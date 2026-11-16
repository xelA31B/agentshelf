"""Reference implementation of AgentShelf scoring.md (v0.3.0) used to check fixtures. QA only; not part of the plugin."""
import json, sys
from decimal import Decimal, ROUND_HALF_UP
LEVEL_W={"REQUIRED":2,"RECOMMENDED":1,"OPTIONAL":0,"EXPERIMENTAL":0}
PTS={"PASS":1,"PARTIAL":0.5,"FAIL":0,"NOT_CHECKED":0}
CAT_W={"access":15,"product_data":25,"policies":15,"feeds":10,"action_path":15,"apis":5,"wallet":15}
BLOCKERS={"ACCESS_BLOCKED","CAPTCHA_DETECTED","LOGIN_BEFORE_PRICE","APP_ONLY_PAYMENT"}
def r(x,nd): q=Decimal(1).scaleb(-nd); return float(Decimal(str(x)).quantize(q,rounding=ROUND_HALF_UP))
def score(fx):
    cats={}; tw=0; tc=0; crit_unknown=False
    for c in fx["checks"]:
        if c["status"]=="NOT_APPLICABLE": continue
        w=LEVEL_W[c["level"]]
        if c.get("critical") and c["status"]=="NOT_CHECKED": crit_unknown=True
        if w==0: continue
        d=cats.setdefault(c["category"],[0,0,0]); d[0]+=w*PTS[c["status"]]; d[1]+=w
        if c["status"]!="NOT_CHECKED": d[2]+=w
        tw+=w; tc+= w if c["status"]!="NOT_CHECKED" else 0
    excl=set(fx.get("excluded_categories",[]))
    num=den=0; out={}
    for k,(e,t,ch) in cats.items():
        if k in excl: continue
        s=10*e/t; out[k]=r(s,1); num+=CAT_W[k]*s/10; den+=CAT_W[k]
    cov=100*tc/tw if tw else 0
    overall=100*num/den if den else None
    if cov<50: status="INCONCLUSIVE"; overall=None
    elif cov>=80 and not crit_unknown: status="FINAL"
    else: status="PROVISIONAL"
    blockers=[b for b in fx.get("blockers",[]) if b in BLOCKERS]
    purchase="NO" if blockers else fx.get("path_fully_observed") and "NOT_VERIFIED" or "PARTLY"
    return {"overall":None if overall is None else r(overall,0),"status":status,"coverage":r(cov,0),"categories":out,"purchase":purchase}
if __name__=="__main__":
    fails=0
    for f in sys.argv[1:]:
        fx=json.load(open(f)); got=score(fx); exp=fx["expected"]
        bad={k:(got[k],v) for k,v in exp.items() if got.get(k)!=v}
        print(("PASS " if not bad else "FAIL ")+fx["name"], "" if not bad else bad); fails+=bool(bad)
    sys.exit(1 if fails else 0)
