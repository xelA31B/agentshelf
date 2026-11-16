"""QA checks for AgentShelf main branch. Usage: python3 validate.py <path-to-plugin-checkout>"""
import sys, json, glob, re, os, subprocess
root=sys.argv[1]; ok=True
def chk(c,msg):
    global ok; print(("ok   " if c else "FAIL ")+msg); ok&=bool(c)
for f in [".claude-plugin/plugin.json",".claude-plugin/marketplace.json"]:
    try: json.load(open(os.path.join(root,f))); chk(True,f+" parses")
    except Exception as e: chk(False,f"{f}: {e}")
import yaml
for f in glob.glob(root+"/skills/*/SKILL.md")+glob.glob(root+"/commands/*.md"):
    fm=yaml.safe_load(open(f).read().split("---")[1]); chk("description" in fm, os.path.relpath(f,root)+" frontmatter")
v=json.load(open(root+"/.claude-plugin/plugin.json"))["version"]
for f in glob.glob(root+"/skills/*/SKILL.md"):
    chk(f'version: "{v}"' in open(f).read(), os.path.relpath(f,root)+f" version {v}")
s=open(root+"/skills/agent-commerce-audit/references/result-schema.md").read()
j=json.loads(re.search(r"```json\n(.*?)```",s,re.S).group(1)); chk(j["plugin_version"]==v,"result-schema example parses, version matches")
pat=re.compile(r"\{\{|\$\{|\{[a-z_]+\}|password|secret|credential|api[_ -]?key|cookie|curl |wget |\btokens?\b",re.I)
hits=[(f,l) for f in glob.glob(root+"/**/*.md",recursive=True)+glob.glob(root+"/.claude-plugin/*.json") for l in open(f) if pat.search(l)]
chk(not hits,"no policy-sensitive wording or brace placeholders"+("" if not hits else f": {hits[:3]}"))
r=subprocess.run([sys.executable,os.path.join(os.path.dirname(__file__),"score.py")]+sorted(glob.glob(os.path.join(os.path.dirname(__file__),"fixtures/*.json"))),capture_output=True,text=True)
print(r.stdout.strip()); chk(r.returncode==0,"scoring fixtures")
sys.exit(0 if ok else 1)
