import os
import base64
import asyncio
from playwright.async_api import async_playwright

work_dir = r"c:\Users\bhara\CascadeProjects\whatsapp-tracker\HouseWarmingVideo"
assets_dir = os.path.join(work_dir, "elegant_assets")
output_scenes_dir = os.path.join(work_dir, "master_scene_pngs")
os.makedirs(output_scenes_dir, exist_ok=True)

# 5 Master Scenes definition (Vertical 1080x1920)
scenes = [
    {
        "id": "scene1_ganesha",
        "bg": os.path.join(assets_dir, "scene1_ganesha.jpg"),
        "html": """
        <div class="scene-overlay lower-layout">
          <div class="glass-card full-card">
            <div class="header-badge">॥ శ్రీ విఘ్నేశ్వర ప్రసన్నః ॥</div>
            <div class="title-sub">అబ్బూరి వారి నూతన</div>
            <div class="title-main">గృహప్రవేశ ఆహ్వానము</div>
            <div class="flourish">
              <div class="f-line"></div>
              <div class="f-symbol">🪔 ❖ 🪔</div>
              <div class="f-line"></div>
            </div>
            <div class="sub-text">
              మా నూతన గృహ ప్రవేశ శుభ తరుణాన<br>
              తామందరూ సకుటుంబంగా విచ్చేసి ఆశీర్వదించగలరు 🙏
            </div>
          </div>
        </div>
        """
    },
    {
        "id": "scene2_muhurtham",
        "bg": os.path.join(assets_dir, "scene2_gomatha.jpg"),
        "html": """
        <div class="scene-overlay lower-layout">
          <div class="glass-card full-card">
            <div class="header-badge">॥ శ్రీరస్తు • శుభమస్తు ॥</div>
            <div class="badge-pill">మొదటి రోజు (Day 1) - సుముహూర్తం</div>
            <div class="date-highlight">05 నవంబర్ 2026</div>
            <div class="day-time">గురువారం రాత్రి గం॥ 9:54 నిమిషాలకు</div>
            <div class="flourish">
              <div class="f-line"></div>
              <div class="f-symbol">🪔 ❖ 🪔</div>
              <div class="f-line"></div>
            </div>
            <div class="sub-text-bold">
              ఉత్తరఫల్గుణీ నక్షత్రయుక్త మిధునలగ్న శుభపుష్కరాంశమునందు<br>
              <span class="gold-highlight">నూతన గృహప్రవేశం మరియు గోపూజ</span>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": "scene3_vratam",
        "bg": os.path.join(assets_dir, "scene3_vratam.jpg"),
        "html": """
        <div class="scene-overlay lower-layout">
          <div class="glass-card full-card">
            <div class="header-badge">॥ శ్రీ సత్యనారాయణ స్వామి ప్రసన్నః ॥</div>
            <div class="badge-pill">రెండవ రోజు (Day 2) - వ్రతం & విందు</div>
            <div class="date-highlight">06 నవంబర్ 2026</div>
            <div class="day-time">శుక్రవారం ఉదయం & మధ్యాహ్నం</div>
            <div class="flourish">
              <div class="f-line"></div>
              <div class="f-symbol">🌸 ❖ 🌸</div>
              <div class="f-line"></div>
            </div>
            <div class="event-line">
              <span class="gold-bullet">✦</span>
              <span><strong>ఉదయం 8:00 AM:</strong> శ్రీ సత్యనారాయణ స్వామి వారి వ్రతం</span>
            </div>
            <div class="event-line highlight-gold">
              <span class="gold-bullet">✦</span>
              <span><strong>విందు (Lunch):</strong> మధ్యాహ్నం 12:00 గంటలకు</span>
            </div>
            <div class="sub-text-sm" style="margin-top: 10px;">
              సకుటుంబంగా స్వామివారి తీర్థప్రసాదములు స్వీకరించి ఆశీర్వదించగలరు 🙏
            </div>
          </div>
        </div>
        """
    },
    {
        "id": "scene4_venue",
        "bg": os.path.join(assets_dir, "scene4_red_curtain.jpg"),
        "html": """
        <div class="scene-overlay center-layout">
          <div class="glass-card full-card">
            <div class="header-badge">॥ గృహప్రవేశ వేదిక ॥</div>
            <div class="badge-pill">వేదిక (Venue Address)</div>
            
            <div class="venue-main">మా స్వగృహము నందు</div>
            <div class="venue-village">కుందురువారిపాలెం గ్రామం</div>
            
            <div class="flourish">
              <div class="f-line"></div>
              <div class="f-symbol">📍 ❖ 📍</div>
              <div class="f-line"></div>
            </div>
            
            <div class="venue-details" style="font-size: 38px; font-weight: 700; color: #FFFFFF; line-height: 1.5; margin-bottom: 12px;">
              ముప్పాళ్ళ మండలం, పల్నాడు జిల్లా
            </div>
            
            <div class="location-landmark" style="font-size: 32px; font-weight: 600; color: #FFE599; margin-bottom: 24px;">
              (సత్తెనపల్లి - నరసరావుపేట సమీపంలో)
            </div>

            <div class="sub-text" style="font-size: 32px; color: #FFF3C4; line-height: 1.5;">
              మా నూతన గృహ ప్రవేశ శుభ తరుణాన<br>
              తామందరూ విచ్చేసి మమ్ములను ఆశీర్వదించగలరు 🙏
            </div>
          </div>
        </div>
        """
    },
    {
        "id": "scene5_welcome",
        "bg": os.path.join(assets_dir, "scene5_welcome.jpg"),
        "html": """
        <div class="scene-overlay center-layout">
          <div class="glass-card full-card">
            <div class="header-badge">॥ సదా మీ రాకను కోరుతూ... ॥</div>
            <div class="badge-pill">~ ఆహ్వానించువారు ~</div>
            
            <div class="host-name">అబ్బూరి వీరభద్రరావు - వెంకటరత్నం</div>
            <div class="host-sub">కుమారులు: భరత్ సాయికుమార్, సునీల్ కుమార్</div>
            <div class="host-family">మరియు అబ్బూరి కుటుంబ సభ్యులు, బంధుమిత్రులు</div>
            
            <div class="contact-pill">
              <span>📞 సంప్రదించండి: <strong>9492902838</strong></span>
            </div>
            
            <div class="tagline-box">
              <div class="see-you-eng">🏡 "See You At Our New Home! ✨"</div>
              <div class="see-you-tel">మా నూతన గృహంలో కలుసుకుందాం!</div>
              <div class="blessing-text">మీ రాకే మాకు ఆనందం • మీ ఆశీస్సులే మాకు శ్రీరామరక్ష 🙏</div>
            </div>
          </div>
        </div>
        """
    }
]

html_template = """<!DOCTYPE html>
<html lang="te">
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@500;600;700;800;900&family=Peddana&family=Ramabhadra&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1080px;
    height: 1920px;
    overflow: hidden;
    background: #000;
    font-family: 'Noto Sans Telugu', 'Ramabhadra', sans-serif;
    position: relative;
    color: #fff;
  }
  
  .bg-image {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.94) contrast(1.04);
  }

  .border-frame {
    position: absolute;
    inset: 22px;
    border: 2px solid rgba(255, 215, 0, 0.55);
    border-radius: 24px;
    pointer-events: none;
    box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.7), 0 0 20px rgba(255, 215, 0, 0.35);
    z-index: 10;
  }

  .scene-overlay {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    padding: 60px 48px;
    z-index: 5;
  }

  .top-only {
    justify-content: flex-start;
    align-items: center;
    padding-top: 80px;
  }

  .split-layout {
    justify-content: space-between;
    align-items: center;
    padding-top: 75px;
    padding-bottom: 75px;
  }

  .center-layout {
    justify-content: center;
    align-items: center;
    padding: 50px 40px;
  }

  .lower-layout {
    justify-content: flex-end;
    align-items: center;
    padding: 60px 40px 100px 40px;
  }

  .glass-card {
    background: linear-gradient(180deg, rgba(32, 4, 10, 0.88) 0%, rgba(20, 2, 6, 0.82) 100%);
    border: 1.5px solid rgba(255, 215, 0, 0.55);
    border-radius: 24px;
    padding: 34px 42px;
    text-align: center;
    width: 960px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.85), 0 0 20px rgba(255, 215, 0, 0.2);
    backdrop-filter: blur(8px);
  }

  .top-compact { padding: 26px 38px; }
  .bottom-compact { padding: 22px 34px; }
  .full-card { padding: 46px 42px; }

  .header-badge {
    font-size: 32px;
    font-weight: 700;
    color: #FFE599;
    letter-spacing: 2px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.95), 0 0 15px rgba(255, 215, 0, 0.6);
    margin-bottom: 12px;
  }

  .badge-pill {
    display: inline-block;
    padding: 8px 30px;
    background: rgba(90, 12, 22, 0.9);
    border: 1.5px solid #FFD700;
    border-radius: 30px;
    color: #FFF3C4;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: 1px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.8), 0 0 12px rgba(255, 215, 0, 0.4);
    margin-bottom: 14px;
  }

  .title-sub {
    font-size: 42px;
    font-weight: 800;
    color: #FFF3C4;
    text-shadow: 0 3px 6px rgba(0,0,0,0.95);
    margin-bottom: 4px;
  }

  .title-main {
    font-family: 'Peddana', serif;
    font-size: 82px;
    font-weight: 900;
    line-height: 1.15;
    background: linear-gradient(180deg, #FFFFFF 0%, #FFF5D6 30%, #FFDF6B 60%, #E69D00 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 4px rgba(0,0,0,0.95)) drop-shadow(0 0 25px rgba(255, 215, 0, 0.75));
    margin-bottom: 12px;
  }

  .date-highlight {
    font-family: 'Peddana', serif;
    font-size: 74px;
    font-weight: 900;
    line-height: 1.15;
    background: linear-gradient(180deg, #FFFFFF 0%, #FFF5D6 30%, #FFDF6B 60%, #E69D00 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 4px rgba(0,0,0,0.95)) drop-shadow(0 0 20px rgba(255, 215, 0, 0.8));
    margin-bottom: 6px;
  }

  .day-time {
    font-size: 36px;
    font-weight: 800;
    color: #FFF3C4;
    text-shadow: 0 3px 6px rgba(0,0,0,0.95);
  }

  .venue-main {
    font-size: 40px;
    font-weight: 800;
    color: #FFF3C4;
    text-shadow: 0 3px 6px rgba(0,0,0,0.95);
    margin-bottom: 4px;
  }

  .venue-village {
    font-family: 'Peddana', serif;
    font-size: 74px;
    font-weight: 900;
    line-height: 1.15;
    background: linear-gradient(180deg, #FFFFFF 0%, #FFF5D6 30%, #FFDF6B 60%, #E69D00 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 4px rgba(0,0,0,0.95)) drop-shadow(0 0 20px rgba(255, 215, 0, 0.75));
  }

  .venue-details {
    font-size: 34px;
    color: #FFFFFF;
    line-height: 1.5;
  }
  .location-landmark {
    font-size: 28px;
    color: #FFE599;
  }

  .host-name {
    font-family: 'Peddana', serif;
    font-size: 66px;
    font-weight: 900;
    line-height: 1.2;
    background: linear-gradient(180deg, #FFFFFF 0%, #FFF5D6 30%, #FFDF6B 60%, #E69D00 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 4px rgba(0,0,0,0.95)) drop-shadow(0 0 20px rgba(255, 215, 0, 0.75));
    margin-bottom: 8px;
  }

  .host-sub {
    font-size: 34px;
    font-weight: 700;
    color: #FFF3C4;
    text-shadow: 0 3px 6px rgba(0,0,0,0.95);
    margin-bottom: 6px;
  }

  .host-family {
    font-size: 30px;
    font-weight: 600;
    color: #FFE699;
    text-shadow: 0 3px 6px rgba(0,0,0,0.95);
    margin-bottom: 16px;
  }

  .flourish {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 440px;
    margin: 12px auto;
  }
  .f-line {
    flex: 1;
    height: 1.5px;
    background: linear-gradient(90deg, transparent, #FFDF6B, #DF9E15, transparent);
  }
  .f-symbol {
    font-size: 22px;
    color: #FFDF6B;
    margin: 0 14px;
    text-shadow: 0 0 10px rgba(255, 223, 107, 0.95);
  }

  .sub-text {
    font-size: 32px;
    font-weight: 600;
    line-height: 1.55;
    color: #FFFFFF;
  }

  .sub-text-bold {
    font-size: 32px;
    font-weight: 600;
    line-height: 1.55;
    color: #FFFFFF;
  }

  .gold-highlight {
    color: #FFD700;
    font-weight: 800;
  }

  .event-line {
    font-size: 32px;
    color: #FFF3C4;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
  }

  .highlight-gold {
    color: #FFE599;
    font-size: 34px;
  }

  .gold-bullet {
    color: #FFD700;
    font-size: 20px;
  }

  .sub-text-sm {
    font-size: 28px;
    color: #FFFFFF;
    margin-top: 10px;
  }

  .contact-pill {
    display: inline-block;
    padding: 10px 34px;
    background: rgba(15, 60, 25, 0.85);
    border: 1.5px solid #4CAF50;
    border-radius: 35px;
    color: #E8F5E9;
    font-size: 30px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.8), 0 0 12px rgba(76, 175, 80, 0.4);
    margin-bottom: 16px;
  }

  .tagline-box {
    background: rgba(70, 10, 20, 0.92);
    border: 2px solid #FFD700;
    border-radius: 20px;
    padding: 16px 28px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.8), 0 0 20px rgba(255, 215, 0, 0.4);
  }

  .see-you-eng {
    font-size: 38px;
    font-weight: 900;
    color: #FFE699;
    letter-spacing: 1px;
    margin-bottom: 6px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.95), 0 0 15px rgba(255, 215, 0, 0.8);
  }

  .see-you-tel {
    font-size: 32px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 8px;
  }

  .blessing-text {
    font-size: 30px;
    font-weight: 700;
    color: #FFD700;
    text-shadow: 0 2px 4px rgba(0,0,0,0.95);
  }
</style>
</head>
<body>
  <img class="bg-image" src="BG_DATA_SRC">
  <div class="border-frame"></div>
  CONTENT_BODY
</body>
</html>"""

async def render_master_pngs():
    print("Rendering 5 master PNGs with Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1920})
        
        for sc in scenes:
            with open(sc["bg"], "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
            bg_data_src = f"data:image/jpeg;base64,{b64}"
            
            full_html = html_template.replace("BG_DATA_SRC", bg_data_src).replace("CONTENT_BODY", sc["html"])
            
            await page.set_content(full_html)
            await page.wait_for_timeout(800)
            
            png_path = os.path.join(output_scenes_dir, f"{sc['id']}.png")
            await page.screenshot(path=png_path)
            print(f"Rendered: {png_path} ({os.path.getsize(png_path):,} bytes)")
            
        await browser.close()
    print("All 5 master PNGs rendered successfully!")

if __name__ == "__main__":
    asyncio.run(render_master_pngs())
