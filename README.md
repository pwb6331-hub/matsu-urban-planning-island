# 連江縣政府工務處都計建管科 - 四鄉五島業務、考核與公文效能 3D 生態島

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-brightgreen?style=for-the-badge&logo=github)](https://pwb6331-hub.github.io/matsu-urban-planning-island/)
[![WebGL](https://img.shields.io/badge/WebGL-Three.js_0.160.0-blue?style=for-the-badge&logo=three.js)](https://threejs.org/)
[![License](https://img.shields.io/badge/連江縣政府工務處-都計建管科-orange?style=for-the-badge)](https://www.matsu.gov.tw)

> 🏛️ **GitHub Pages 線上展示網址（手機、平板、桌機皆可直接連線）：**  
> 🔗 **[https://pwb6331-hub.github.io/matsu-urban-planning-island/](https://pwb6331-hub.github.io/matsu-urban-planning-island/)**

---

## 📌 專案列管代號與本機路徑
- **報告列管案號**：`REPORT:E/115/都計建管業務/都計建管業務控管表/3D動態島資料`
- **本機檔案位置**：`E:\2026GEM-SKILL\115\都計建管業務\都計建管業務控管表\3D動態島資料\`
- **點擊直接開啟本機網頁**：[index.html](file:///E:/2026GEM-SKILL/115/都計建管業務/都計建管業務控管表/3D動態島資料/index.html)

---

## ⚡ 高階 WebGL 架構與效能優化亮點

1. **GPU Custom Shader 海浪引擎（0% CPU 頂點開銷）**：
   - 廢除傳統 CPU 逐幀迭代 8,281 個頂點與 PCIe 緩衝區上傳，改由 `MeshStandardMaterial.onBeforeCompile` 注入頂點與片段著色器（三波疊加 + 浪峰白沫 Crest Foam 混色），僅更新單一 `uTime` Uniform。
2. **硬體實例化渲染 (`THREE.InstancedMesh`) 與資源快取池 (`ResourcePool`)**：
   - 將四島環道植栽與共用幾何/材質統一收斂至 `ResourcePool` 與 `InstancedMesh` 批次渲染，大幅降低 WebGL Draw Calls 與記憶體配置。
3. **階層式座標空間修正與三時相動態光源**：
   - 修正建築窗戶發光面片世界座標偏移問題，完整掛載於南竿福澳倉儲、北竿芹壁石屋、東引燈塔機房與莒光大埔聚落局部座標系，並為媽祖巨神像燈籠配置夜間真實點光源 (`THREE.PointLight`)。
4. **跨平台真實時間步進 (`THREE.Clock` Delta-Time) 與背景休眠機制**：
   - 全面解耦螢幕刷新率（支援 30Hz / 60Hz / 120Hz ProMotion / 144Hz 等速運鏡與航行），並整合 `visibilitychange` 頁面生命週期監聽，切換至背景分頁時自動暫停 WebGL 與 Web Audio 渲染。
5. **雙相機模式（`📐 等距微縮 Orthographic` / `🎥 透視景深 Perspective`）與貝茲樣條海運網路**：
   - 支援一鍵切換等距正交微縮沙盒與透視景深視角；導入 `THREE.CatmullRomCurve3` 閉環樣條航線（南北之星、臺馬之星、東海明珠三航道），船隻依切線向量 (`getTangentAt`) 真實轉向並附帶船尾浪花。

---

## 🚀 快速開啟與部署方式

### 方式 1：直接雙擊開啟（本機無伺服器模式）
- 雙擊執行目錄下的 [`open_local.bat`](file:///E:/2026GEM-SKILL/115/都計建管業務/都計建管業務控管表/3D動態島資料/open_local.bat)，即可在預設瀏覽器直接開啟 3D 生態島。
- 本網頁採用純單一 HTML 與標準 CDN 架構，支援 `file:///` 協定直接瀏覽。

### 方式 2：本機 HTTP 伺服器（適合手機與平板同一區網測試）
- 雙擊執行目錄下的 [`open_http_server.bat`](file:///E:/2026GEM-SKILL/115/都計建管業務/都計建管業務控管表/3D動態島資料/open_http_server.bat)。
- 終端機將啟動 `http://localhost:8080/`，同 Wi-Fi 區網下的手機或平板只要輸入電腦 IP（如 `http://192.168.x.x:8080/`）即可實機操作。

### 方式 3：GitHub Pages 自動部署與同步
- 雙擊執行目錄下的 [`deploy.bat`](file:///E:/2026GEM-SKILL/115/都計建管業務/都計建管業務控管表/3D動態島資料/deploy.bat)。
- 腳本將自動執行 `git add`、`git commit` 並推播至遠端儲存庫 `pwb6331-hub/matsu-urban-planning-island`。
- 推播後約 1 分鐘即可於線上展示網址 [https://pwb6331-hub.github.io/matsu-urban-planning-island/](https://pwb6331-hub.github.io/matsu-urban-planning-island/) 查閱最新版本。

---

## 🏝️ 四鄉五島微縮地理與業務特色模型

1. **南竿行政核心示範島**
   - **微縮特徵**：福澳港混凝土碼頭、貨運裝卸吊臂、夜間呼吸金光媽祖巨神像。
   - **主管同仁**：曹玲、陳國華、葉大魁。
   - **職掌範疇**：違建管理、南竿私人建使照施工勘驗、建築公安與設備安檢、介壽整體開發案、公部門建使照督考。

2. **北竿芹壁傳統聚落保存島**
   - **微縮特徵**：花崗石人字砌石屋、壓瓦石防颱屋頂、朱紅起翹封火山牆、外海芹壁龜島。
   - **主管同仁**：陳國華、曹文馨、葉大魁。
   - **職掌範疇**：芹壁聚落保存區建築管制與室裝許可、北竿私人建使照勘驗、建築線指示、塘岐整體開發、四鄉五島都計樁聯測。

3. **東引國之北疆要塞島**
   - **微縮特徵**：18 世紀歐風純白花崗岩圓柱燈塔、紅色鑄鐵圓頂、360 度旋轉探照光束。
   - **主管同仁**：張宇涵、曹文馨、陳國華。
   - **職掌範疇**：都計保/公專案通盤檢討（第二階段）、東引私人建使照勘驗、山坡地建築管制（建築管理無水保審驗）。

4. **莒光樂活雙心島 (東西莒)**
   - **微縮特徵**：東莒白犬燈塔花崗岩塔身、大埔傳統聚落石屋、雙心穿梭客輪。
   - **主管同仁**：曹玲、陳國華、曹曉芳。
   - **職掌範疇**：莒光私人建使照勘驗、大埔聚落舊有合法房屋證明、建築物無障礙設施設備安全檢查。

---

## 📊 115 年度全科公文效能與業務考評總結

- **發文總數**：累計 **1,710 件**（不含存查與未創號）。
- **平均辦結速度**：**1.45 天**，公文時效優良指標達 **99.2%**。
- **年度考評榮譽**：
  - 違章建築考核：偏遠型第一名（嘉獎一次）、進步獎（嘉獎二次）。
  - 施工管理考核：偏遠型第一名（記功一次）。
  - 建造執照考核：偏遠型第三名（嘉獎二次）。
  - 無障礙考核：偏遠型第二名。
  - 土地利用監測評鑑：貢獻獎（嘉獎二次）、模範銅獎。

---

## 📞 諮詢窗口

- **主辦機關**：連江縣政府工務處 都市計畫建築管理科
- **機關地址**：連江縣南竿鄉介壽村 76 號 3 樓
- **官方網站**：[連江縣政府全球資訊網](https://www.matsu.gov.tw)
