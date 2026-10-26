# कॉन्फ़िगरेशन गाइड — CRT Smart Entry Pro

सेटिंग्स इंडिकेटर पर **⚙ Settings → Inputs** में मिलती हैं। ग्रुप 1–5 (CORE) इंडिकेटर और स्ट्रैटेजी दोनों में एक जैसे हैं। सिग्नल मिलाने हों तो दोनों में ये सेटिंग्स समान रखें।

---

## 1 · CRT Range

| सेटिंग | डिफ़ॉल्ट | व्याख्या |
|---|---|---|
| **Range Source** | Higher Timeframe Candle | रेफ़रेंस रेंज कहाँ से आए (नीचे विस्तार से)। |
| Higher Timeframe | 60 | सिर्फ़ HTF मोड के लिए। यह चार्ट टाइमफ्रेम से **बड़ा** होना चाहिए, नहीं तो स्क्रिप्ट स्पष्ट runtime error दिखाती है। |
| Opening Range Duration | 15 मिनट | सिर्फ़ "Session Opening Range" के लिए। सेशन शुरू होने के बाद पहले N मिनट। |
| First Candle Size | 15 | सिर्फ़ "First Session Candle" के लिए: पहली 5m या 15m कैंडल। |
| Reset pending setups when a new range starts | ऑन | नई रेंज आने पर पुराने पेंडिंग सेटअप हटाता है। "Previous Candle" मोड में लागू नहीं होता। |
| Max signals per range (per direction) | 1 | एक रेंज पर एक दिशा में अधिकतम सिग्नल। इससे बार-बार सिग्नल नहीं बनते। |

### Range Source के विकल्प
1. **Previous Candle:** पिछली बंद हुई चार्ट कैंडल का हाई/लो। हर कैंडल पर नई रेंज बनती है (क्लासिक 2–3 कैंडल CRT)। पेंडिंग सेटअप अपने स्वीप लेवल की कॉपी रखते हैं और टाइमआउट से ख़त्म होते हैं।
2. **Higher Timeframe Candle:** चुने गए HTF की **पिछली बंद** कैंडल। नई HTF कैंडल शुरू होते ही नई रेंज आती है। उदाहरण: 5m चार्ट पर HTF = 60, या 15m चार्ट पर HTF = 240।
3. **Session Opening Range:** सेशन की शुरुआत से N मिनट तक का हाई/लो। विंडो बंद होने पर रेंज लॉक होती है, उससे पहले स्टेटस "Building" रहता है।
4. **First Session Candle (5m/15m):** Opening Range ही, बस अवधि 5 या 15 मिनट। चार्ट TF इस अवधि से ≤ होना चाहिए। बड़ा हो तो पहली चार्ट कैंडल ही रेंज बनती है, और डैशबोर्ड चेतावनी दिखाता है।
5. **Custom Session:** "Custom Range Session" विंडो (जैसे `0000-0600` एशिया सेशन) का हाई/लो। विंडो ख़त्म होने पर रेंज लॉक होती है। रात-पार (overnight) विंडो भी चलती है, जैसे `2000-0200`।

> सेशन-आधारित मोड (3, 4, 5) के लिए **इंट्राडे चार्ट** चाहिए। Daily/Weekly चार्ट पर डैशबोर्ड चेतावनी देता है।

---

## 1b · Sessions & Timezone

| सेटिंग | डिफ़ॉल्ट | व्याख्या |
|---|---|---|
| **Session Start Source** | Symbol Session (auto) | **Auto:** सिंबल का अपना रेगुलर सेशन, जो TradingView से आता है (`session.isfirstbar_regular`)। हर मार्केट के लिए अपने-आप सही होता है। **Manual:** नीचे वाला session string और timezone। |
| Manual Trading Session | `0000-0000` | सिर्फ़ Manual मोड में। `0000-0000` का मतलब 24 घंटे है; नया सेशन चुने गए timezone के हर नए दिन पर शुरू होता है। |
| Custom Range Session | `0000-0600` | Custom Session रेंज की विंडो। |
| Timezone | Exchange | `Exchange` = सिंबल के एक्सचेंज का timezone। अन्य उदाहरण: `Asia/Kolkata`, `UTC`, `America/New_York`, `Europe/London`, `GMT+5:30`। |
| Only allow entries inside a signal session | ऑफ़ | ऑन करने पर BUY/SELL सिर्फ़ "Signal Session" के अंदर बनते हैं। बाहर बनने वाली एंट्री रीसेट हो जाती है। |
| Signal Session | `0000-0000` | एंट्री की अनुमति वाली विंडो। |

### ओवरनाइट मार्केट्स और 24/7 क्रिप्टो
- **क्रिप्टो (24/7):** Session Start Source = Manual, Manual Trading Session = `0000-0000`, Timezone = `UTC`। तब हर UTC दिन 00:00 पर नया सेशन शुरू होगा। Auto मोड भी काम करता है (TradingView पर क्रिप्टो का "दिन" आमतौर पर 00:00 UTC से शुरू होता है)। फिर भी Manual + UTC ज़्यादा स्पष्ट है।
- **फ़्यूचर्स/कमोडिटी (ओवरनाइट, जैसे शाम 6 बजे से अगले दिन शाम 5 बजे):** Auto मोड सबसे भरोसेमंद है। Manual में ओवरनाइट session string दें, जैसे `1800-1700`, और सही timezone, जैसे `America/New_York`।
- **फॉरेक्स:** Custom Session से London (`0700-1000`, `Europe/London`) या New York (`0930-1130`, `America/New_York`) की रेंज बनाएँ। या HTF 240/D इस्तेमाल करें।
- **भारतीय इंडेक्स/स्टॉक्स:** Auto मोड NSE/BSE का सेशन अपने-आप लेता है। Manual में चाहें तो `0915-1530` और `Asia/Kolkata`।
- **Extended hours:** Auto मोड **रेगुलर** सेशन की पहली कैंडल लेता है। अगर आपको प्री-मार्केट से रेंज चाहिए, तो Manual session दें।

---

## 2 · Liquidity Sweep

| सेटिंग | डिफ़ॉल्ट | व्याख्या |
|---|---|---|
| **Sweep Detection** | Wick | **Wick:** हाई/लो का रेंज के पार जाना ही स्वीप है। **Close Beyond:** कैंडल को रेंज के बाहर **क्लोज़** भी होना होगा, और रिक्लेम बाद की कैंडल पर ही हो सकता है। इसके लिए "Max bars to confirm" ≥ 1 रखें। |
| **Sweep Confirmation** | Close Back Inside | **Close Back Inside:** रेंज के अंदर वापस क्लोज़। **Rejection Candle:** अंदर क्लोज़ + सही दिशा की कैंडल बॉडी + रिजेक्शन विक ≥ चुना गया %। |
| Max bars to confirm (reclaim) | 3 | स्वीप के बाद रिक्लेम के लिए अधिकतम कैंडल्स। 0 = स्वीप वाली कैंडल पर ही। |
| Minimum Sweep Distance | None, 0 | स्वीप की न्यूनतम गहराई: **Ticks** (× mintick), **ATR Multiple** (× ATR), **% of Range**। छोटे शोर-भरे स्वीप फ़िल्टर करने के लिए। |
| Rejection wick ≥ % of candle | 40 | सिर्फ़ Rejection Candle मोड में। |

स्वीप "पेंडिंग" (SWEPT) तब तक रहता है जब तक कन्फर्मेशन न हो। चार्ट पर **SW** मार्कर और "Liquidity Sweep" अलर्ट **कन्फर्म्ड** स्वीप पर आते हैं। रिक्लेम के बाद प्राइस फिर स्वीप लेवल के पार क्लोज़ हो, तो सेटअप वापस पेंडिंग में चला जाता है और एक्सट्रीम अपडेट होता है।

---

## 3 · Market Structure Shift

| सेटिंग | डिफ़ॉल्ट | व्याख्या |
|---|---|---|
| Pivot Left Bars | 3 | स्विंग की बाईं ओर कितनी कैंडल्स कम/ज़्यादा हों। |
| **Pivot Right Bars (confirmation delay)** | 2 | स्विंग की दाईं ओर कितनी कैंडल्स **बंद** होने के बाद वह कन्फर्म हो। **यही जानबूझकर किया गया डिले है।** बड़ा मान रखने से स्विंग ज़्यादा भरोसेमंद होंगे, लेकिन MSS देर से आएगा। |
| MSS Break Type | Close | **Close:** स्विंग के पार कैंडल का क्लोज़ ज़रूरी (सुझाया गया)। **Wick:** सिर्फ़ विक का पार जाना काफ़ी। |
| Max bars from sweep confirmation to MSS | 20 | इतने में MSS न हो तो सेटअप इनवैलिड। |
| Max swing age (bars) | 100 | इससे पुराने स्विंग MSS या स्ट्रक्चर-स्टॉप के लिए इस्तेमाल नहीं होते। |

**MSS लेवल का चयन:** बुलिश केस में, स्वीप कन्फर्म होते समय वर्तमान क्लोज़ के **ऊपर** वाला सबसे हाल का **कन्फर्म्ड** स्विंग हाई चुना जाता है। उस समय कोई स्विंग न हो, तो आगे की कैंडल्स पर (नए कन्फर्म्ड स्विंग्स में से) खोजा जाता है। बेयरिश केस इसका उल्टा है। MSS हमेशा अगली कैंडल से ही गिना जाता है, स्वीप-कन्फर्मेशन वाली कैंडल पर नहीं।

---

## 4 · Entry

| सेटिंग | डिफ़ॉल्ट | व्याख्या |
|---|---|---|
| **Entry Mode** | Confirmation | **Confirmation (MSS close):** MSS कैंडल के क्लोज़ पर सिग्नल। **Retest of MSS level:** MSS के बाद प्राइस टूटे लेवल को (± tolerance) छुए, फिर लेवल के सही तरफ़ और सही दिशा की कैंडल के साथ क्लोज़ हो। |
| Retest tolerance (× ATR) | 0.10 | रिटेस्ट कितना पास होना चाहिए। |
| Max bars to wait for retest | 10 | इतने में रिटेस्ट न हो तो सेटअप इनवैलिड। |

रिटेस्ट का इंतज़ार करते समय अगर प्राइस **स्वीप एक्सट्रीम के पार** क्लोज़ हो जाए, तो सेटअप इनवैलिड हो जाता है।

---

## 5 · Stop Loss & Targets

| सेटिंग | डिफ़ॉल्ट | व्याख्या |
|---|---|---|
| **Stop-Loss Method** | Beyond Sweep Extreme | **Sweep Extreme:** स्वीप का सबसे निचला लो (बुलिश) / सबसे ऊँचा हाई (बेयरिश), साथ में बफ़र। **Structure Swing:** एंट्री के नीचे (बुलिश) / ऊपर (बेयरिश) का सबसे हाल का कन्फर्म्ड स्विंग, साथ में बफ़र। न मिले तो स्वीप एक्सट्रीम लिया जाता है। **ATR Based:** एंट्री ± ATR × मल्टीपल। |
| ATR Length | 14 | |
| ATR Stop Multiple | 1.5 | सिर्फ़ ATR मोड में। |
| Stop Buffer (× ATR) | 0.05 | एक्सट्रीम/स्विंग से अतिरिक्त दूरी। ATR मोड पर लागू नहीं होता। |
| Max Risk (× ATR, 0 = off) | 0 | रिस्क इससे ज़्यादा हो तो सिग्नल नहीं बनता। |
| Target 1 / T2 / T3 (R) | 1 / 2 / 3 | टार्गेट = Entry ± R-multiple × Risk। |
| Move stop to break-even after T1 | ऑफ़ | T1 के बाद SL को एंट्री पर ले जाता है। |

**वैलिडेशन:** SL और टार्गेट्स `mintick` पर राउंड होते हैं। इसके बाद अगर रिस्क ≤ ½ tick हो (यानी SL ग़लत साइड पर या शून्य दूरी पर), या SL निकाला ही न जा सके, तो सिग्नल जनरेट नहीं होता। टार्गेट्स हमेशा असली रिस्क से निकाले जाते हैं, फ़िक्स्ड पॉइंट्स से नहीं।

---

## 6 · Visuals (सिर्फ़ इंडिकेटर)

| सेटिंग | डिफ़ॉल्ट | नोट |
|---|---|---|
| Range High / Low lines, Midpoint | ऑन | `plot()` से बनती हैं, इसलिए ऑब्जेक्ट लिमिट पर असर नहीं। "Building" रेंज फीके रंग में दिखती है। |
| Sweep markers / MSS markers | ऑन | `plotshape()`, पूरी हिस्ट्री। |
| MSS level lines | ऑन | डैश्ड लाइन, जो स्विंग से ब्रेक कैंडल तक जाती है। "MSS lines kept" से सीमित। |
| BUY/SELL labels (with prices) | ऑन | Entry और SL लिखा होता है। टूलटिप में T1–T3 और रिस्क। "Trades with labels kept" से सीमित। |
| BUY/SELL arrows | ऑन | पूरी हिस्ट्री (plotshape)। |
| Entry / SL / T1 / T2 / T3 lines | ऑन | "Trades with level lines kept" (डिफ़ॉल्ट 3) तक ही रहती हैं; पुरानी डिलीट हो जाती हैं। |
| Price tags on latest trade levels | ऑन | सिर्फ़ आख़िरी ट्रेड पर 5 रीयूज़ होने वाले लेबल। |
| Shaded risk / reward zones | ऑफ़ | रिस्क (Entry–SL) और रिवॉर्ड (Entry–T3) के बॉक्स। |
| Provisional sweep hints | ऑफ़ | लाइव कैंडल पर `sw?`। **सिग्नल नहीं** है और गायब हो सकता है। |

**ऑब्जेक्ट बजट (अधिकतम):** लाइनें = 5 × level history (≤50) + MSS lines (≤100) ≤ 350। लेबल ≤ 200 + 5। बॉक्स ≤ 100। ये सब TradingView की 500 की सीमा के अंदर हैं। पुराने ऑब्जेक्ट्स अपने-आप डिलीट होते रहते हैं।

## 7 · Dashboard
दिखाई जाने वाली जानकारी:
- सिंबल · TF, Range Source, रेंज High/Low/Mid और रेंज स्टेटस (No range / Building / Active / low/high swept)
- Bull/Bear सेटअप स्टेट
- आख़िरी सिग्नल की दिशा, Entry, SL (BE हुआ हो तो साथ में), T1/T2/T3, Risk और R:R
- सिग्नल स्टेटस ("CONFIRMED · active T1✓", "Closed · Stop loss" …)
- Note पंक्ति: चेतावनियाँ, या आख़िरी इनवैलिडेशन का कारण

## 8 · Alerts
"Enable dynamic alert() messages" ऑन हो, तो "Any alert() function call" वाले अलर्ट में पूरा विवरण आता है। `alertcondition()` वाले अलर्ट हमेशा उपलब्ध रहते हैं। विवरण: README.md → अलर्ट्स।

---

## 9 · Strategy-only सेटिंग्स

| सेटिंग | डिफ़ॉल्ट | व्याख्या |
|---|---|---|
| Trade Direction | Long & Short | Long Only / Short Only। अनुमति न होने वाली दिशा का सेटअप बिना ऑर्डर के consume हो जाता है। |
| **Position Sizing** | Risk % of Equity | **Fixed Quantity**, **% of Equity** (पोज़िशन वैल्यू), **Risk % of Equity** (SL लगने पर ≈ X% नुकसान, जिसकी सीमा "Max position value" तय करता है)। |
| Quantity step / lot size | 1 | मात्रा इस step पर **नीचे** राउंड होती है। F&O में लॉट साइज़ डालें (एक्सचेंज के मौजूदा लॉट साइज़ ख़ुद जाँचें)। क्रिप्टो में 0.001 आदि। मात्रा 0 बने तो ऑर्डर नहीं जाता। |
| Partial exits at T1/T2/T3 | ऑन | % closed at T1 और T2। बाकी T3 पर। T1% + T2% < 100 होना चाहिए। |
| Single target | T2 | पार्शियल्स ऑफ़ हों तो पूरी पोज़िशन इसी टार्गेट पर। |
| Recalculate targets from actual fill price | ऑन | फ़िल के बाद टार्गेट्स फ़िल प्राइस से। SL नहीं बदलता। अगर फ़िल पहले ही SL के पार हो, तो पोज़िशन तुरंत बंद होती है। |
| Use date range / Start / End / Close after End | ऑफ़ | सिर्फ़ इस अवधि में एंट्री। |
| Properties टैब | | Initial capital (100000), कमीशन (0.03%), स्लिपेज (2 ticks), Bar Magnifier। अपने मार्केट के अनुसार बदलें। |

---

## मार्केट-वार शुरुआती प्रीसेट (केवल शुरुआती बिंदु, गारंटी नहीं)

| परिदृश्य | चार्ट TF | Range Source | अन्य |
|---|---|---|---|
| NIFTY/BANKNIFTY ओपनिंग रेंज | 3m या 5m | First Session Candle → 15 | Auto session; Max bars to MSS 15; SL = Sweep Extreme |
| इंडेक्स इंट्राडे HTF | 5m | HTF → 60 | Signal session चाहें तो `0930-1500` / `Asia/Kolkata` |
| स्टॉक्स स्विंग | 1H | HTF → D | Pivot 3/3; Retest entry |
| BTC/ETH | 15m | HTF → 240 | Manual `0000-0000`, UTC; Min sweep 0.1 ATR |
| BTC एशिया रेंज | 5m | Custom Session `0000-0600` | Timezone `UTC`; Signal session `0700-1600` |
| EURUSD लंदन | 5m | Custom Session `0000-0700` | Timezone `Europe/London`; Signal session `0700-1100` |
| Gold/Crude फ़्यूचर्स | 15m | HTF → 240 | Auto session |

## समस्या निवारण
- **"Higher Timeframe must be greater than the chart timeframe":** HTF बढ़ाएँ, या चार्ट TF घटाएँ।
- **कोई सिग्नल नहीं:** डैशबोर्ड की "Note" और सेटअप स्टेट देखें। फिर ये आज़माएँ:
  - Max signals per range बढ़ाएँ।
  - टाइमआउट बढ़ाएँ।
  - Minimum sweep distance घटाएँ।
  - Pivot Right Bars घटाएँ।
- **"Warming up":** चार्ट पर पर्याप्त हिस्ट्री नहीं है (ATR/पिवट के लिए कम से कम कुछ दर्जन कैंडल्स चाहिए)।
- **रेंज "Building" में ही अटकी:** सेशन/timezone सेटिंग जाँचें। Custom session string उसी timezone में होनी चाहिए जो सेटिंग में चुना है।
- **Heikin Ashi/Renko चार्ट:** ये सिंथेटिक कैंडल्स हैं। सिग्नल और बैकटेस्ट भ्रामक हो सकते हैं। स्टैंडर्ड कैंडल्स इस्तेमाल करें।
