import sys
import base64

head = '''
<html>
  <head>
	<title>Tier List Maker</title>
	<style>
	  :root {
		  --muted: #3a3a3a;
		  --tier1: #f45353;
		  --tier2: #2598fc;
		  --tier3: #c681a5;
		  --tier4: #069e36;
		  --tier5: #a281c6;
		  --tier6: #6ea7c1;
		  --tier7: #d1bb19;
		  --tier8: #ba854c;
		  --tier9: #394432;
		  --tier10: #3d290c;
			  
	  }
	  body {
		  background-color: black;
		  color: white;
		  font-family: Ubuntu Mono, Inconsolata, monospace;
	  }
	  td.main {
		  width: 100%;
	  }
	  td.sidebar {
		  width: 400px;
		  min-width: 400px;
		  position: relative;
		  padding: 0px;
	  }
	  td.sidebar > .title-wrapper {
		  position: absolute;
		  height: content;
		  top: 10px;
	  }
	  .tier {
		  border-spacing: 10px;
	  }
	  .tier .label {
		  height: 96px;
		  width: 96px;
		  min-width: 6rem;
		  text-align: center;
		  font-size: 64px;
		  font-weight: bold;
	  }
	  .tier tr:nth-of-type(1) .label {
		  background-color: var(--tier1);
	  }
	  .tier tr:nth-of-type(2) .label {
		  background-color: var(--tier2);
	  }
	  .tier tr:nth-of-type(3) .label {
		  background-color: var(--tier3);
	  }
	  .tier tr:nth-of-type(4) .label {
		  background-color: var(--tier4);
	  }
	  .tier tr:nth-of-type(5) .label {
		  background-color: var(--tier5);
	  }
	  .tier tr:nth-of-type(6) .label {
		  background-color: var(--tier6);
	  }
	  .tier tr:nth-of-type(7) .label {
		  background-color: var(--tier7);
	  }
	  .tier tr:nth-of-type(8) .label {
		  background-color: var(--tier8);
	  }
	  .tier tr:nth-of-type(9) .label {
		  background-color: var(--tier9);
	  }
	  .tier tr:nth-of-type(10) .label {
		  background-color: var(--tier10);
	  }
	  .tier .elements {
		  background-color: var(--muted);
		  height: 96px;
		  width: 100%;
		  padding: 0px;
	  }
	  div.elc {
		  padding: 2px;
		  height: 100%;
		  width: 100%;
	  }
	  img:not(.big) {
		  min-height: 0px;
		  min-width: 0px;
		  height: 88px;
		  margin: 2px;
	  }
	  img.big {
		  max-width: 400px;
		  max-height: 400px;
	  }
	  h1 {
		  margin: 0px;
	  }
	</style>
	<script>
	  window.ondragstart = function() {return false;}
	  
	  window.onload = function() {
		console.log("ok");
		var se = null;
		
		let ts = document.querySelectorAll("img:not(.big)");
		let bi = document.getElementById("bi");
		let bt = document.getElementById("bt");
		let tws = document.querySelectorAll(".tw");
		
		ts.forEach(t => {
		  t.addEventListener("click", function(e) {
			e.stopPropagation();
			e.preventDefault();
			if (se == this) {
			  se = null;
			  bi.setAttribute("src", "");
			  bt.innerHTML = "---";
			  return false;
			}
			se = this;
			bi.setAttribute("src", this.getAttribute("src"));
			bt.innerHTML = this.getAttribute("n");
		  });
		});
		tws.forEach(tw => {
		  tw.addEventListener("click", function(e) {
			if (se === null) {
			  return false;
			}
			e.stopPropagation();
			e.preventDefault();
			this.querySelector(".elc").appendChild(se);
			//se = null;
			//bi.setAttribute("src", "");
			//bt.innerHTML = "---";
		  });
		});
	  };
	</script>
  </head>
  <body>
	<table class="wrapper"><tr>
		<td class="main">
		  <table class="tier">
			<tr class="tw">
			  <td class="label tier1">S</td>
			  <td class="elements">
				<div class="elc"></div>
			  </td>
			</tr>
			<tr class="tw">
			  <td class="label tier2">A</td>
			  <td class="elements">
				<div class="elc"></div>
			  </td>
			</tr>
			<tr class="tw">
			  <td class="label tier3">B</td>
			  <td class="elements">
				<div class="elc"></div>
			  </td>
			</tr>
			<tr class="tw">
			  <td class="label tier4">C</td>
			  <td class="elements">
				<div class="elc"></div>
			  </td>
			</tr>
			<tr class="tw">
			  <td class="label tier5">D</td>
			  <td class="elements">
				<div class="elc"></div>
			  </td>
			</tr>
			<tr class="tw">
			  <td class="label tier6">F</td>
			  <td class="elements">
				<div class="elc"></div>
			  </td>
			</tr>
		  </table>
		</td>
		<td class="sidebar">
		  <div class="title-wrapper">
			<h1 id="bt">---</h1>
			<div style="height: 400px;">
			  <img class="big" id="bi"/>
			</div>
			<div class="tw" style="min-height: 450px;">
			  <div class="elc">'''
tail = '''</div>
</div>
</div>
</td>
</tr></table>
</body>
</html>
'''
imgs = ''

for fp in sys.argv[2:]:
    fti = fp.rfind('.')
    fni = max(fp.rfind('/'), fp.rfind('\\'))
    ft = fp[fti+1:]
    if fti >= 0 and ft in ['png', 'jpeg', 'jpg', 'exr', 'tiff', 'gif', 'webp', 'jfif']:
        fn = fp[fni+1:fti]
        with open(fp, "rb") as img:
            src=base64.b64encode(img.read()).decode('utf-8')
            imgs += f'<img src="data:image/{ft};base64,{src}" n="{fn}"/>'
    else:
        print(f'unrecognized file type {fp}, skipping')

with open(sys.argv[1], "w") as f:
    f.write(head + imgs + tail)
