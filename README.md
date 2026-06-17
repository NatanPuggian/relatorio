# Mapeamento de Ações × Resultados — Arena (Copa 2026)

Painel visual que cruza as **ações de cada afiliado** com os **resultados** (cadastros, FTD, CPA e comissão) durante a 1ª semana da Copa (10 a 16/06/2026).

## Arquivos

- **`index.html`** — o site, arquivo único e autossuficiente. É só abrir no navegador (duplo-clique). Usa Chart.js via CDN.
- **`build_site.py`** — gerador. Lê `data.json` e reescreve o `index.html`.
- **`data.json`** — dados já tratados (56 registros Dia × Afiliado × Ação).
- **`mapeamento_afiliados (semana 10 a 16) (1).xlsx`** — planilha-fonte original.

## Como regerar

Se a planilha/dados mudarem:

```bash
python build_site.py
```

## Seções do painel

1. KPIs da semana
2. Leitura rápida (insights)
3. Ranking de afiliados (barra + rosca + tabela ordenável)
4. Linha do tempo — filtrável por afiliado
5. Por afiliado (funil cadastro → FTD → CPA, evolução diária, histórico de ações)
6. O que cada tipo de ação entregou
7. **Playbook** — melhores ações por afiliado, base para programar a próxima semana
8. Base completa filtrável

## Principais leituras (semana 10–16/06)

- **Concentração:** Mateus Caumo = 50,8% de toda a comissão; com Gol do Rayo, 73%.
- **CPA sustenta:** 90,3% da comissão veio de CPA fixo; rev. share ficou negativo em 2 dias.
- **BETGO (16/06):** 2.089 cadastros num dia, mas só 7,9% viraram CPA — qualificação ainda não maturou.
- **Brasil em campo:** 13/06 (Garantida do Brasil) foi o pico, R$ 123k.
