# -*- coding: utf-8 -*-
import json

rows = json.load(open('data.json', encoding='utf-8'))['rows']
DATA_JS = json.dumps(rows, ensure_ascii=False)

HTML = r'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Arena · Mapeamento de Ações × Resultados · Copa 2026</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<style>
:root{
  --bg:#0a0e14; --bg2:#0f141d; --card:#141b26; --card2:#1a2230;
  --line:#222c3a; --txt:#e8edf4; --mut:#8a96a8; --mut2:#5d6personally;
  --grn:#19e08f; --grn2:#0bb673; --lime:#b6ff3d; --gold:#ffce4f;
  --red:#ff5c6c; --blu:#4aa8ff; --pur:#9d7bff; --orange:#ff9f45;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--txt);font-family:'Segoe UI',system-ui,-apple-system,sans-serif;
  line-height:1.5;-webkit-font-smoothing:antialiased;overflow-x:hidden}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
a{color:inherit}
h1,h2,h3{font-weight:800;letter-spacing:-.02em;line-height:1.12}
.mut{color:var(--mut)}
.tag{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  color:var(--grn);background:rgba(25,224,143,.1);border:1px solid rgba(25,224,143,.25);
  padding:5px 11px;border-radius:99px}

/* HERO */
header{position:relative;padding:64px 0 30px;overflow:hidden;
  background:radial-gradient(1100px 460px at 78% -8%,rgba(25,224,143,.16),transparent 60%),
             radial-gradient(720px 360px at 8% 6%,rgba(74,168,255,.08),transparent 60%);
  border-bottom:1px solid var(--line)}
header h1{font-size:clamp(30px,5vw,52px);margin:16px 0 10px}
header h1 .hl{color:var(--grn)}
header .sub{font-size:clamp(15px,2vw,18px);color:var(--mut);max-width:680px}
.period{margin-top:8px;font-size:13px;color:var(--lime);font-weight:600}

/* KPI */
.kpis{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin:34px 0 6px}
.kpi{background:linear-gradient(160deg,var(--card),var(--bg2));border:1px solid var(--line);
  border-radius:16px;padding:18px 18px 16px;position:relative;overflow:hidden}
.kpi::before{content:'';position:absolute;inset:0 auto auto 0;width:100%;height:3px;
  background:linear-gradient(90deg,var(--grn),transparent)}
.kpi .lab{font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--mut);font-weight:700}
.kpi .val{font-size:clamp(22px,3vw,30px);font-weight:800;margin-top:8px;letter-spacing:-.02em}
.kpi .sub2{font-size:12px;color:var(--mut);margin-top:4px}
.kpi.grn .val{color:var(--grn)} .kpi.gold .val{color:var(--gold)}

/* SECTION */
section{padding:50px 0}
.sec-h{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:6px}
.sec-h h2{font-size:clamp(22px,3vw,30px)}
.sec-h .num{font-size:13px;font-weight:800;color:var(--grn);font-family:monospace}
.sec-desc{color:var(--mut);max-width:720px;margin-bottom:26px;font-size:15px}

/* INSIGHTS */
.insights{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.ins{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--grn);
  border-radius:14px;padding:20px 22px;position:relative}
.ins.warn{border-left-color:var(--gold)} .ins.bad{border-left-color:var(--red)}
.ins.info{border-left-color:var(--blu)}
.ins .ico{font-size:22px}
.ins h3{font-size:17px;margin:8px 0 7px}
.ins p{font-size:14px;color:var(--mut);line-height:1.55}
.ins p b{color:var(--txt);font-weight:700}
.ins .big{font-size:26px;font-weight:800;color:var(--grn);letter-spacing:-.02em}
.ins.warn .big{color:var(--gold)} .ins.bad .big{color:var(--red)} .ins.info .big{color:var(--blu)}

/* CARD */
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px}
.grid2{display:grid;grid-template-columns:1.45fr 1fr;gap:20px}
.chart-box{position:relative;height:340px}
.chart-box.sm{height:280px}
.card-t{font-size:15px;font-weight:700;margin-bottom:4px}
.card-d{font-size:13px;color:var(--mut);margin-bottom:16px}

/* TABLE */
table{width:100%;border-collapse:collapse;font-size:13.5px}
th,td{padding:10px 12px;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}
th:first-child,td:first-child{text-align:left}
th{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--mut);font-weight:700;
  cursor:pointer;user-select:none;position:sticky;top:0;background:var(--card)}
th:hover{color:var(--grn)}
tbody tr:hover{background:var(--card2)}
.pos{color:var(--grn)} .neg{color:var(--red)}
.af-dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:8px;vertical-align:middle}
.bar-cell{position:relative}
.bar-cell .fill{position:absolute;left:0;top:50%;transform:translateY(-50%);height:60%;
  border-radius:4px;opacity:.16;z-index:0}
.bar-cell span{position:relative;z-index:1}

/* AFFILIATE SELECTOR */
.af-tabs{display:flex;gap:9px;flex-wrap:wrap;margin-bottom:24px}
.af-tab{background:var(--card);border:1px solid var(--line);border-radius:99px;padding:9px 16px;
  font-size:13.5px;font-weight:600;cursor:pointer;transition:.15s;display:flex;align-items:center;gap:8px}
.af-tab:hover{border-color:var(--mut)}
.af-tab.active{background:var(--grn);color:#04130c;border-color:var(--grn)}
.af-tab.active .af-dot{display:none}
.af-panel{display:grid;grid-template-columns:1fr 1.3fr;gap:20px;align-items:start}
.af-stats{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.af-stat{background:var(--bg2);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.af-stat .l{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);font-weight:700}
.af-stat .v{font-size:23px;font-weight:800;margin-top:4px}
.af-stat .v small{font-size:13px;color:var(--mut);font-weight:600}
.funnel{margin-top:4px}
.fbar{margin:10px 0}
.fbar .ft{display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px}
.fbar .ft b{font-weight:700}
.fbar .track{height:13px;background:var(--bg2);border-radius:7px;overflow:hidden}
.fbar .fl{height:100%;border-radius:7px;transition:width .6s cubic-bezier(.2,.8,.2,1)}
.af-actions{margin-top:18px}
.af-actions h4{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--mut);margin-bottom:10px}
.aev{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid var(--line);font-size:13.5px;align-items:flex-start}
.aev .ad{font-family:monospace;font-size:12px;color:var(--mut);min-width:42px;padding-top:1px}
.aev .ax{flex:1}
.aev .ax .obs{display:inline-block;font-size:10.5px;font-weight:700;color:var(--gold);
  background:rgba(255,206,79,.12);border-radius:5px;padding:1px 7px;margin-left:6px}
.aev .av{text-align:right;font-weight:700;min-width:90px}
.aev .av small{display:block;font-size:11px;color:var(--mut);font-weight:500}

/* ACTION CATEGORY */
.cats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:8px}
.catc{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px}
.catc h3{font-size:16px;margin-bottom:3px}
.catc .cd{font-size:12px;color:var(--mut);margin-bottom:14px}
.catc .row{display:flex;justify-content:space-between;font-size:13px;padding:6px 0;border-top:1px solid var(--line)}
.catc .row b{font-weight:700}
.catc .qbadge{font-size:11px;font-weight:700;padding:2px 9px;border-radius:99px}

/* TIMELINE legend */
.tl-head{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;margin-bottom:16px;flex-wrap:wrap}
.tl-sel{display:flex;align-items:center;gap:9px}
.tl-sel label{font-size:12px;color:var(--mut);font-weight:600}
.tl-sel select{background:var(--bg2);color:var(--txt);border:1px solid var(--line);border-radius:9px;
  padding:8px 13px;font-size:13.5px;font-family:inherit;font-weight:600;cursor:pointer}
.tl-sel select:hover{border-color:var(--grn)}
.tl-ev{display:flex;gap:18px;flex-wrap:wrap;margin-top:16px}
.tl-ev .e{display:flex;gap:8px;align-items:center;font-size:12.5px;color:var(--mut)}
.tl-ev .e b{color:var(--txt)}
.tl-ev .e .m{font-size:16px}

/* filter bar */
.fbar2{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px;align-items:center}
.fbar2 select{background:var(--card);color:var(--txt);border:1px solid var(--line);border-radius:9px;
  padding:8px 12px;font-size:13px;font-family:inherit}
.fbar2 label{font-size:12px;color:var(--mut);font-weight:600}

/* playbook */
.play{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.pc{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;position:relative;overflow:hidden}
.pc::before{content:'';position:absolute;top:0;left:0;width:4px;height:100%;background:var(--afc,var(--grn))}
.pc .ph{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px}
.pc .ph .pn{display:flex;align-items:center;gap:10px;font-size:18px;font-weight:800}
.pc .ph .ptot{text-align:right} .pc .ph .ptot .pv{font-size:18px;font-weight:800}
.pc .ph .ptot .pl{font-size:10.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);font-weight:700}
.pblock{background:var(--bg2);border:1px solid var(--line);border-radius:11px;padding:13px 15px;margin-bottom:11px}
.pblock .bl{font-size:10.5px;text-transform:uppercase;letter-spacing:.09em;color:var(--mut);font-weight:700;margin-bottom:5px;display:flex;align-items:center;gap:6px}
.pblock .bv{font-size:14.5px;font-weight:600}
.pblock .bv .res{color:var(--grn);font-weight:800}
.pblock .bv .day{font-family:monospace;font-size:12px;color:var(--mut)}
.prec{background:linear-gradient(135deg,rgba(25,224,143,.1),transparent);border:1px solid rgba(25,224,143,.22);
  border-radius:11px;padding:13px 15px}
.prec .bl{color:var(--grn)}
.prec .bv{font-size:13.5px;color:var(--txt);line-height:1.5;font-weight:500}
.prec .bv b{color:var(--grn);font-weight:700}

footer{border-top:1px solid var(--line);padding:30px 0 50px;color:var(--mut);font-size:13px;text-align:center}

@media(max-width:920px){
  .kpis{grid-template-columns:repeat(2,1fr)}
  .insights{grid-template-columns:1fr}
  .grid2{grid-template-columns:1fr}
  .af-panel{grid-template-columns:1fr}
  .cats{grid-template-columns:1fr}
  .play{grid-template-columns:1fr}
}
.scrollx{overflow-x:auto}
</style>
</head>
<body>
<header>
  <div class="wrap">
    <span class="tag">Arena · Inteligência de Afiliação</span>
    <h1>Mapeamento de <span class="hl">Ações × Resultados</span><br>na 1ª semana de Copa</h1>
    <p class="sub">Cruzamento entre o que cada afiliado <b>fez</b> (ações, garantidas, lançamentos) e o que cada ação <b>gerou</b> em cadastros, depósitos, CPAs e comissão.</p>
    <p class="period">● Período: 10 a 16 de junho de 2026 · 7 dias · 8 afiliados</p>
    <div class="kpis" id="kpis"></div>
    <p class="mut" style="font-size:12.5px;margin-top:14px">Role para ver os destaques, o ranking, a linha do tempo e a análise individual de cada afiliado.</p>
  </div>
</header>

<section style="padding-top:46px">
  <div class="wrap">
    <div class="sec-h"><span class="num">01</span><h2>Leitura rápida da semana</h2></div>
    <p class="sec-desc">Os pontos que mais saltam dos números — o que puxou resultado, o que enganou e onde está o risco.</p>
    <div class="insights" id="insights"></div>
  </div>
</section>

<section style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-h"><span class="num">02</span><h2>Ranking de afiliados</h2></div>
    <p class="sec-desc">Comissão final gerada no período e o peso de cada um no total da operação. Clique nos cabeçalhos da tabela para reordenar.</p>
    <div class="grid2">
      <div class="card">
        <div class="card-t">Comissão final por afiliado</div>
        <div class="card-d">Soma de Rev. share + CPA nos 7 dias (R$)</div>
        <div class="chart-box"><canvas id="rankBar"></canvas></div>
      </div>
      <div class="card">
        <div class="card-t">Participação no total</div>
        <div class="card-d">Quanto cada um representa da comissão final</div>
        <div class="chart-box"><canvas id="shareDonut"></canvas></div>
      </div>
    </div>
    <div class="card" style="margin-top:20px">
      <div class="scrollx"><table id="rankTable"></table></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><span class="num">03</span><h2>Linha do tempo</h2></div>
    <p class="sec-desc">Evolução dia a dia. Veja a operação inteira ou isole um afiliado para enxergar o ritmo individual dele na semana.</p>
    <div class="card">
      <div class="tl-head">
        <div>
          <div class="card-t" id="tlTitle">Comissão final, cadastros e CPAs por dia</div>
          <div class="card-d">Barras = comissão final (R$) · linhas = funil de volume (cadastros → FTDs → CPAs qualificados)</div>
        </div>
        <div class="tl-sel">
          <label>Ver:</label>
          <select id="tlAf"><option value="">Operação completa</option></select>
        </div>
      </div>
      <div class="chart-box"><canvas id="timeline"></canvas></div>
      <div class="tl-ev">
        <div class="e"><span class="m">🇧🇷</span><span><b>13/06 — Garantida do Brasil:</b> pico da semana, R$123k</span></div>
        <div class="e"><span class="m">⚠️</span><span><b>12/06 — Dia da restrição:</b> rev. share fica negativo</span></div>
        <div class="e"><span class="m">🚀</span><span><b>16/06 — Lançamento BETGO:</b> cadastro recorde, mas CPA despenca</span></div>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-h"><span class="num">04</span><h2>Por afiliado</h2></div>
    <p class="sec-desc">Selecione um afiliado para ver o funil cadastro → depósito → CPA, a evolução diária e o histórico de ações com resultado.</p>
    <div class="af-tabs" id="afTabs"></div>
    <div class="af-panel">
      <div>
        <div class="af-stats" id="afStats"></div>
        <div class="card" style="margin-top:16px">
          <div class="card-t">Funil de conversão</div>
          <div class="card-d" id="afFunnelD"></div>
          <div class="funnel" id="afFunnel"></div>
        </div>
      </div>
      <div class="card">
        <div class="card-t">Comissão final por dia</div>
        <div class="card-d" id="afDayD"></div>
        <div class="chart-box sm"><canvas id="afDayChart"></canvas></div>
        <div class="af-actions">
          <h4>Ações no período</h4>
          <div id="afActions"></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><span class="num">05</span><h2>O que cada tipo de ação entregou</h2></div>
    <p class="sec-desc">Agrupando as ações por natureza. A métrica-chave é a <b>qualificação</b> (CPA ÷ FTD): de cada depositante, quantos viraram CPA pago. Volume alto sem qualificação é dinheiro que não entra.</p>
    <div class="cats" id="cats"></div>
  </div>
</section>

<section style="background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-h"><span class="num">06</span><h2>Playbook · melhores ações por afiliado</h2></div>
    <p class="sec-desc">Para cada afiliado: a ação campeã da semana, o tipo de ação que mais entregou CPA por ocorrência e uma recomendação prática para programar a próxima semana. Ordenado por comissão gerada.</p>
    <div class="play" id="play"></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-h"><span class="num">07</span><h2>Base completa · Dia × Afiliado × Ação</h2></div>
    <p class="sec-desc">Todos os 56 registros cruzados. Filtre por afiliado ou por dia.</p>
    <div class="fbar2">
      <label>Afiliado</label><select id="fAf"><option value="">Todos</option></select>
      <label>Dia</label><select id="fDay"><option value="">Todos</option></select>
    </div>
    <div class="card"><div class="scrollx"><table id="fullTable"></table></div></div>
  </div>
</section>

<footer>
  <div class="wrap">
    Arena · Mapeamento de ações e resultados — Copa 2026 · Semana 10–16/06 · Gerado a partir do arquivo de mapeamento de afiliados.
  </div>
</footer>

<script>
const DATA = __DATA__;
const BRL = n => 'R$ '+Math.round(n).toLocaleString('pt-BR');
const BRLk = n => Math.abs(n)>=1000 ? 'R$ '+(n/1000).toFixed(n>=10000?0:1).replace('.',',')+'k' : 'R$ '+Math.round(n);
const NUM = n => Math.round(n).toLocaleString('pt-BR');
const PCT = n => (n).toFixed(1).replace('.',',')+'%';
const AFS = [...new Set(DATA.map(r=>r.af))];
const DAYS = [...new Set(DATA.map(r=>r.d))].sort();
const COL = {'Mateus Caumo':'#19e08f','Gol do Rayo':'#4aa8ff','El Barba':'#ffce4f','Vitor ZZ':'#9d7bff',
  'Rennan':'#ff9f45','Ah Maria':'#ff5c6c','Cabreloa':'#2ed4c6','Dupla Aposta':'#7a8aff'};
const sum=(a,k)=>a.reduce((s,r)=>s+r[k],0);
const byAf=a=>DATA.filter(r=>r.af===a);
const byDay=d=>DATA.filter(r=>r.d===d);
const dlab=d=>{const[,,dd]=d.split('-');return dd+'/06';};

Chart.defaults.color='#8a96a8';
Chart.defaults.font.family="'Segoe UI',system-ui,sans-serif";
Chart.defaults.font.size=12;

// ---- KPIs ----
const T={reg:sum(DATA,'reg'),ftd:sum(DATA,'ftd'),cpa:sum(DATA,'cpa'),rev:sum(DATA,'rev'),ccpa:sum(DATA,'ccpa'),fin:sum(DATA,'fin')};
document.getElementById('kpis').innerHTML=[
  ['Cadastros',NUM(T.reg),'novos registros'],
  ['FTD',NUM(T.ftd),PCT(T.ftd/T.reg*100)+' dos cadastros depositaram'],
  ['CPA qualificados',NUM(T.cpa),PCT(T.cpa/T.ftd*100)+' dos FTDs viraram CPA'],
  ['Comissão final','grn|'+BRLk(T.fin),'no período de 7 dias'],
  ['CPA = base da receita','gold|'+PCT(T.ccpa/T.fin*100),'da comissão vem de CPA fixo'],
].map(k=>{
  let v=k[1],cls='';if(v.includes('|')){[cls,v]=v.split('|');}
  return `<div class="kpi ${cls}"><div class="lab">${k[0]}</div><div class="val">${v}</div><div class="sub2">${k[2]}</div></div>`;
}).join('');

// ---- INSIGHTS ----
const ag=AFS.map(a=>({a,fin:sum(byAf(a),'fin'),cpa:sum(byAf(a),'cpa'),reg:sum(byAf(a),'reg'),ftd:sum(byAf(a),'ftd')})).sort((x,y)=>y.fin-x.fin);
const lead=ag[0], lead2=ag[0].fin+ag[1].fin;
const d16=byDay('2026-06-16'), d13=byDay('2026-06-13');
const ins=[
  ['grn','📊','Concentração na operação',
   `<span class="big">${PCT(lead.fin/T.fin*100)}</span> de toda a comissão final saiu de <b>${lead.a}</b>. Somando com ${ag[1].a}, dois afiliados respondem por <b>${PCT(lead2/T.fin*100)}</b> do resultado — força hoje, risco de dependência amanhã.`],
  ['info','🧱','O CPA é quem sustenta',
   `<span class="big">${PCT(T.ccpa/T.fin*100)}</span> da comissão veio de <b>CPA fixo</b>. O rev. share oscilou e fechou só ${BRLk(T.rev)} — em 2 dias ficou <b>negativo</b>. A receita previsível está no volume qualificado, não na sorte da casa.`],
  ['warn','🚀','BETGO: muito barulho, pouca qualificação',
   `O lançamento de 16/06 trouxe <b>${NUM(sum(d16,'reg'))} cadastros</b> num único dia (39% da semana), mas só <span class="big">${PCT(sum(d16,'cpa')/sum(d16,'reg')*100)}</span> viraram CPA. Casa nova converte cadastro, mas a qualificação ainda não maturou — vale acompanhar o CPA dos próximos dias.`],
  ['grn','🇧🇷','Brasil em campo move a agulha',
   `13/06 (Garantida do Brasil) foi o <b>pico</b>: <span class="big">${BRLk(sum(d13,'fin'))}</span> em comissão, ${NUM(sum(d13,'cpa'))} CPAs. Ação ancorada em jogo do Brasil + garantida é o combo mais forte da semana.`],
];
document.getElementById('insights').innerHTML=ins.map(i=>
  `<div class="ins ${i[0]}"><div class="ico">${i[1]}</div><h3>${i[2]}</h3><p>${i[3]}</p></div>`).join('');

// ---- RANK BAR ----
new Chart(document.getElementById('rankBar'),{type:'bar',data:{labels:ag.map(x=>x.a),
  datasets:[{data:ag.map(x=>x.fin),backgroundColor:ag.map(x=>COL[x.a]),borderRadius:6,barThickness:22}]},
  options:{indexAxis:'y',plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>BRL(c.raw)}}},
  scales:{x:{grid:{color:'#1c2531'},ticks:{callback:v=>BRLk(v)}},y:{grid:{display:false}}}}});

// ---- DONUT ----
new Chart(document.getElementById('shareDonut'),{type:'doughnut',data:{labels:ag.map(x=>x.a),
  datasets:[{data:ag.map(x=>x.fin),backgroundColor:ag.map(x=>COL[x.a]),borderColor:'#141b26',borderWidth:3}]},
  options:{cutout:'62%',plugins:{legend:{position:'right',labels:{boxWidth:10,padding:9,font:{size:11.5}}},
   tooltip:{callbacks:{label:c=>c.label+': '+BRL(c.raw)+' ('+PCT(c.raw/T.fin*100)+')'}}}}});

// ---- RANK TABLE ----
let rankData=AFS.map(a=>{const r=byAf(a);const reg=sum(r,'reg'),ftd=sum(r,'ftd'),cpa=sum(r,'cpa'),fin=sum(r,'fin');
  return{a,reg,ftd,cpa,fin,rev:sum(r,'rev'),conv:reg?ftd/reg*100:0,qual:ftd?cpa/ftd*100:0,share:fin/T.fin*100,perCpa:cpa?fin/cpa:0};});
let rankSort={k:'fin',dir:-1};
const RCOLS=[['a','Afiliado'],['reg','Cadastros'],['ftd','FTD'],['cpa','CPA'],['conv','Conv. FTD'],['qual','Qualif. CPA'],['fin','Comissão final'],['share','% do total']];
function renderRank(){
  rankData.sort((x,y)=>rankSort.k==='a'?x.a.localeCompare(y.a)*rankSort.dir:(y[rankSort.k]-x[rankSort.k])*-rankSort.dir);
  const mx=Math.max(...rankData.map(r=>r.fin));
  let h='<thead><tr>'+RCOLS.map(c=>`<th data-k="${c[0]}">${c[1]}${rankSort.k===c[0]?(rankSort.dir<0?' ▾':' ▴'):''}</th>`).join('')+'</tr></thead><tbody>';
  rankData.forEach(r=>{h+=`<tr>
    <td><span class="af-dot" style="background:${COL[r.a]}"></span>${r.a}</td>
    <td>${NUM(r.reg)}</td><td>${NUM(r.ftd)}</td><td>${NUM(r.cpa)}</td>
    <td>${PCT(r.conv)}</td><td>${PCT(r.qual)}</td>
    <td class="bar-cell"><div class="fill" style="width:${r.fin/mx*100}%;background:${COL[r.a]}"></div><span><b>${BRL(r.fin)}</b></span></td>
    <td>${PCT(r.share)}</td></tr>`;});
  h+='</tbody>';
  const t=document.getElementById('rankTable');t.innerHTML=h;
  t.querySelectorAll('th').forEach(th=>th.onclick=()=>{const k=th.dataset.k;
    if(rankSort.k===k)rankSort.dir*=-1;else rankSort={k,dir:k==='a'?1:-1};renderRank();});
}
renderRank();

// ---- TIMELINE (filtrável por afiliado) ----
const tlAf=document.getElementById('tlAf');
ag.forEach(x=>tlAf.innerHTML+=`<option value="${x.a}">${x.a}</option>`);
let tlChart=null;
function tlSeries(af){
  return DAYS.map(d=>{const r=af?byAf(af).filter(z=>z.d===d):byDay(d);
    return{fin:sum(r,'fin'),reg:sum(r,'reg'),ftd:sum(r,'ftd'),cpa:sum(r,'cpa'),rev:sum(r,'rev')};});
}
function renderTimeline(af){
  const s=tlSeries(af);
  const barColor=af?(s.map(x=>x.rev<0?'#ff5c6c':(COL[af]||'#19e08f'))):s.map(x=>x.rev<0?'#ff5c6c':'#19e08f');
  document.getElementById('tlTitle').textContent=af?('Ritmo de '+af+' · comissão, cadastros e CPAs por dia'):'Comissão final, cadastros e CPAs por dia';
  if(tlChart)tlChart.destroy();
  tlChart=new Chart(document.getElementById('timeline'),{data:{labels:DAYS.map(dlab),
    datasets:[
     {type:'bar',label:'Comissão final',data:s.map(x=>x.fin),backgroundColor:barColor,borderRadius:6,yAxisID:'y',order:4},
     {type:'line',label:'Cadastros',data:s.map(x=>x.reg),borderColor:'#4aa8ff',backgroundColor:'#4aa8ff',
      tension:.3,yAxisID:'y1',pointRadius:4,order:1},
     {type:'line',label:'FTDs',data:s.map(x=>x.ftd),borderColor:'#2ed4c6',backgroundColor:'#2ed4c6',
      tension:.3,yAxisID:'y1',pointRadius:4,order:2},
     {type:'line',label:'CPAs',data:s.map(x=>x.cpa),borderColor:'#ffce4f',backgroundColor:'#ffce4f',
      tension:.3,yAxisID:'y1',pointRadius:4,borderDash:[5,4],order:3}]},
    options:{plugins:{legend:{position:'top',labels:{boxWidth:12,padding:14}},
      tooltip:{callbacks:{label:c=>c.dataset.label+': '+(c.dataset.yAxisID==='y'?BRL(c.raw):NUM(c.raw))}}},
     scales:{y:{position:'left',grid:{color:'#1c2531'},ticks:{callback:v=>BRLk(v)},title:{display:true,text:'Comissão (R$)'}},
      y1:{position:'right',grid:{display:false},title:{display:true,text:'Volume'}}}}});
}
tlAf.onchange=()=>renderTimeline(tlAf.value);
renderTimeline('');

// ---- AFFILIATE PANEL ----
const afTabs=document.getElementById('afTabs');
const afOrder=ag.map(x=>x.a);
afTabs.innerHTML=afOrder.map((a,i)=>`<div class="af-tab${i===0?' active':''}" data-a="${a}"><span class="af-dot" style="background:${COL[a]}"></span>${a}</div>`).join('');
let afChart=null;
function selAf(a){
  afTabs.querySelectorAll('.af-tab').forEach(t=>t.classList.toggle('active',t.dataset.a===a));
  const r=byAf(a),reg=sum(r,'reg'),ftd=sum(r,'ftd'),cpa=sum(r,'cpa'),fin=sum(r,'fin'),rev=sum(r,'rev');
  document.getElementById('afStats').innerHTML=[
    ['Comissão final',BRL(fin),''],['CPA pago',BRL(sum(r,'ccpa')),''],
    ['Cadastros',NUM(reg),''],['CPA qualif.',NUM(cpa),''],
  ].map(s=>`<div class="af-stat"><div class="l">${s[0]}</div><div class="v">${s[1]}</div></div>`).join('');
  // funnel
  const mx=reg||1;
  document.getElementById('afFunnelD').textContent=`De ${NUM(reg)} cadastros, ${NUM(ftd)} depositaram e ${NUM(cpa)} qualificaram CPA`;
  document.getElementById('afFunnel').innerHTML=[
    ['Cadastros',reg,'#4aa8ff',100],
    ['FTD (depósito)',ftd,'#19e08f',ftd/mx*100],
    ['CPA qualificado',cpa,'#ffce4f',cpa/mx*100],
  ].map(f=>`<div class="fbar"><div class="ft"><span>${f[0]}</span><b>${NUM(f[1])} · ${PCT(f[3])}</b></div>
    <div class="track"><div class="fl" style="width:${f[3]}%;background:${f[2]}"></div></div></div>`).join('');
  // day chart
  const dd=DAYS.map(d=>{const x=byAf(a).find(z=>z.d===d);return x?x.fin:0;});
  document.getElementById('afDayD').textContent='Evolução diária de '+a;
  if(afChart)afChart.destroy();
  afChart=new Chart(document.getElementById('afDayChart'),{type:'bar',data:{labels:DAYS.map(dlab),
    datasets:[{data:dd,backgroundColor:dd.map(v=>v<0?'#ff5c6c':COL[a]),borderRadius:5}]},
    options:{plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>BRL(c.raw)}}},
     scales:{x:{grid:{display:false}},y:{grid:{color:'#1c2531'},ticks:{callback:v=>BRLk(v)}}}}});
  // actions
  document.getElementById('afActions').innerHTML=byAf(a).map(x=>`<div class="aev">
    <div class="ad">${dlab(x.d)}</div>
    <div class="ax">${x.acao==='—'?'<span class="mut">sem ação registrada</span>':x.acao}${x.obs?`<span class="obs">${x.obs}</span>`:''}</div>
    <div class="av ${x.fin<0?'neg':''}">${BRL(x.fin)}<small>${x.cpa} CPA · ${x.reg} cad.</small></div></div>`).join('');
}
afTabs.querySelectorAll('.af-tab').forEach(t=>t.onclick=()=>selAf(t.dataset.a));
selAf(afOrder[0]);

// ---- ACTION CATEGORIES ----
function cat(a){a=(a||'').toLowerCase();
  if(a.includes('betgo'))return'Lançamento BETGO';
  if(a.includes('lan')&&a.includes('grupo'))return'Lançamento de grupo';
  if(a.includes('garantid')||a.includes('aumentada')||a.includes('vitória')||a.includes('vit'))return'Garantida / Aumentada';
  if(a.includes('bing'))return'Bingão';
  if(a.includes('normal'))return'Movimentação normal';
  return'Outros';}
const catMap={};
DATA.forEach(r=>{const c=cat(r.acao);(catMap[c]=catMap[c]||[]).push(r);});
const catMeta={'Garantida / Aumentada':['🎯','Aposta garantida ou odd aumentada, geralmente atrelada a um jogo'],
  'Lançamento de grupo':['📣','Abertura de grupo novo (Copa)'],
  'Lançamento BETGO':['🚀','Estreia da casa BETGO'],
  'Bingão':['🎱','Ação de bingo no grupo'],
  'Movimentação normal':['🔁','Dia sem ação especial, rotina do grupo'],
  'Outros':['•','Sem ação classificada']};
const catArr=Object.entries(catMap).map(([c,rs])=>({c,n:rs.length,reg:sum(rs,'reg'),ftd:sum(rs,'ftd'),cpa:sum(rs,'cpa'),fin:sum(rs,'fin'),
  qual:sum(rs,'ftd')?sum(rs,'cpa')/sum(rs,'ftd')*100:0})).sort((a,b)=>b.fin-a.fin);
document.getElementById('cats').innerHTML=catArr.map(c=>{
  const m=catMeta[c.c]||['•',''];
  const q=c.qual, qc=q>=70?'#19e08f':q>=45?'#ffce4f':'#ff5c6c', qbg=q>=70?'rgba(25,224,143,.14)':q>=45?'rgba(255,206,79,.14)':'rgba(255,92,108,.14)';
  const qt=q>=70?'alta':q>=45?'média':'baixa';
  return `<div class="catc"><h3>${m[0]} ${c.c}</h3><div class="cd">${m[1]} · ${c.n} ocorrências</div>
   <div class="row"><span>Comissão final</span><b>${BRL(c.fin)}</b></div>
   <div class="row"><span>Cadastros</span><b>${NUM(c.reg)}</b></div>
   <div class="row"><span>CPA qualificados</span><b>${NUM(c.cpa)}</b></div>
   <div class="row"><span>Qualificação (CPA/FTD)</span><span class="qbadge" style="color:${qc};background:${qbg}">${PCT(c.qual)} · ${qt}</span></div>
   <div class="row"><span>Comissão / dia-ação</span><b>${BRLk(c.fin/c.n)}</b></div></div>`;}).join('');

// ---- PLAYBOOK (melhores ações por afiliado) ----
const CATICON={'Garantida / Aumentada':'🎯','Lançamento de grupo':'📣','Lançamento BETGO':'🚀','Bingão':'🎱','Movimentação normal':'🔁','Outros':'•'};
function playbookFor(a){
  const rows=byAf(a);
  const reg=sum(rows,'reg'),ftd=sum(rows,'ftd'),cpa=sum(rows,'cpa'),fin=sum(rows,'fin');
  const qualA=ftd?cpa/ftd*100:0;
  // best single action (by fin)
  const best=rows.slice().sort((x,y)=>y.fin-x.fin)[0];
  // category stats for this affiliate
  const cm={};
  rows.forEach(r=>{const c=cat(r.acao);(cm[c]=cm[c]||[]).push(r);});
  let cats=Object.entries(cm).map(([c,rs])=>({c,n:rs.length,cpa:sum(rs,'cpa'),fin:sum(rs,'fin'),
    reg:sum(rs,'reg'),ftd:sum(rs,'ftd'),cpaOcc:sum(rs,'cpa')/rs.length,finOcc:sum(rs,'fin')/rs.length,
    qual:sum(rs,'ftd')?sum(rs,'cpa')/sum(rs,'ftd')*100:0}));
  const real=cats.filter(c=>c.c!=='Outros');
  const ranked=(real.length?real:cats).slice().sort((x,y)=>y.cpaOcc-x.cpaOcc);
  const topCat=ranked[0];
  // recommendation engine
  const r=[];
  if(!real.length||fin<2500){
    r.push(`Operação ainda incipiente — quase nenhuma ação estruturada na semana`);
    r.push(`começar simples: uma <b>garantida atrelada a um jogo do Brasil</b> para criar base de CPA antes de escalar volume`);
  }else{
    r.push(`Repetir e dar mais frequência a <b>${topCat.c.toLowerCase()}</b> (entregou ${topCat.cpaOcc.toFixed(1)} CPA por ação)`);
    const garant=cats.find(c=>c.c==='Garantida / Aumentada');
    const norm=cats.find(c=>c.c==='Movimentação normal');
    if(garant&&norm&&garant.cpaOcc>norm.cpaOcc*1.2)
      r.push(`garantida rende ~${(garant.cpaOcc/Math.max(norm.cpaOcc,0.1)).toFixed(1)}× mais CPA que dia normal — ancorar nos jogos fortes da rodada`);
    if(qualA>=65) r.push(`público qualifica muito bem (${PCT(qualA)} CPA/FTD): pode empurrar mais volume com segurança`);
    else if(qualA<45) r.push(`qualificação baixa (${PCT(qualA)} CPA/FTD): segurar lançamentos que só inflam cadastro e focar no que puxa CPA`);
    else r.push(`qualificação mediana (${PCT(qualA)}): subir testando garantidas em jogos de seleção`);
  }
  return{a,reg,ftd,cpa,fin,qualA,best,topCat,reco:r.join('. ')+'.'};
}
document.getElementById('play').innerHTML=afOrder.map(a=>{
  const p=playbookFor(a),c=COL[a];
  const bAct=p.best.acao==='—'?'Sem ação estruturada':p.best.acao;
  return `<div class="pc" style="--afc:${c}">
    <div class="ph">
      <div class="pn"><span class="af-dot" style="background:${c}"></span>${a}</div>
      <div class="ptot"><div class="pv" style="color:${c}">${BRLk(p.fin)}</div><div class="pl">na semana · ${NUM(p.cpa)} CPA</div></div>
    </div>
    <div class="pblock">
      <div class="bl">🏆 Ação campeã <span class="day">${dlab(p.best.d)}</span></div>
      <div class="bv">${bAct} → <span class="res">${BRL(p.best.fin)}</span> · ${p.best.cpa} CPA</div>
    </div>
    <div class="pblock">
      <div class="bl">${CATICON[p.topCat.c]||'•'} Tipo mais eficiente</div>
      <div class="bv">${p.topCat.c} · <b>${p.topCat.cpaOcc.toFixed(1)} CPA por ação</b> <span class="day">(${p.topCat.n}× na semana)</span></div>
    </div>
    <div class="prec">
      <div class="bl">📌 Recomendação p/ próxima semana</div>
      <div class="bv">${p.reco}</div>
    </div>
  </div>`;
}).join('');

// ---- FULL TABLE ----
const fAf=document.getElementById('fAf'),fDay=document.getElementById('fDay');
afOrder.forEach(a=>fAf.innerHTML+=`<option>${a}</option>`);
DAYS.forEach(d=>fDay.innerHTML+=`<option value="${d}">${dlab(d)}</option>`);
function renderFull(){
  let rows=DATA.slice();
  if(fAf.value)rows=rows.filter(r=>r.af===fAf.value);
  if(fDay.value)rows=rows.filter(r=>r.d===fDay.value);
  let h='<thead><tr><th>Dia</th><th>Afiliado</th><th>Ação</th><th>Cad.</th><th>FTD</th><th>CPA</th><th>Rev.</th><th>CPA R$</th><th>Final</th></tr></thead><tbody>';
  rows.forEach(r=>{h+=`<tr><td>${dlab(r.d)}</td><td><span class="af-dot" style="background:${COL[r.af]}"></span>${r.af}</td>
    <td style="text-align:left;white-space:normal;max-width:280px">${r.acao==='—'?'<span class="mut">—</span>':r.acao}${r.obs?` <span style="color:#ffce4f;font-size:11px">(${r.obs})</span>`:''}</td>
    <td>${r.reg}</td><td>${r.ftd}</td><td>${r.cpa}</td>
    <td class="${r.rev<0?'neg':''}">${BRL(r.rev)}</td><td>${BRL(r.ccpa)}</td>
    <td class="${r.fin<0?'neg':'pos'}"><b>${BRL(r.fin)}</b></td></tr>`;});
  const tr=rows;
  h+=`</tbody><tfoot><tr style="border-top:2px solid #2a3646;font-weight:800">
    <td colspan="3">TOTAL (${tr.length})</td><td>${NUM(sum(tr,'reg'))}</td><td>${NUM(sum(tr,'ftd'))}</td><td>${NUM(sum(tr,'cpa'))}</td>
    <td>${BRL(sum(tr,'rev'))}</td><td>${BRL(sum(tr,'ccpa'))}</td><td class="pos">${BRL(sum(tr,'fin'))}</td></tr></tfoot>`;
  document.getElementById('fullTable').innerHTML=h;
}
fAf.onchange=renderFull;fDay.onchange=renderFull;renderFull();
</script>
</body>
</html>'''

HTML = HTML.replace('__DATA__', DATA_JS)
# fix a typo var in css
HTML = HTML.replace('--mut2:#5d6personally;', '--mut2:#5d6675;')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(HTML)
print('index.html escrito:', len(HTML), 'bytes')
