# FEUP Erasmus

A tool that makes use of [sigpy](https://github.com/msramalho/sigpy) to scrape the ERASMUS page at FEUP into JSON files, for time analysis and other fun ideas people usually have.

### Features
 * `python extract.py [USERNAME|201403027] [YEAR|2018]` scrapes all the **current** hardcoded allocations (ids should be updated annually as they are unpredictable) into `archive/COURSE/YEAR/yyyy_mm_dd_hh_mm.json`, this should be executed on a daily basis (or at the rate of the system updates). This folder (`archive`) is gitignored, so it will only persist on your local clone. 
 * `python anonymize.py` since the identity of students and their GPA is not public information it needs to be anonymized, this script takes care of that and creates a duplicate _database_ in `anonymous/COURSE/YEAR/yyyy_mm_dd_hh_mm.json` using funny, yet consistent, anonymous animals for students.
 * Jupyter notebook [discover previous years](discover_previous_years.ipynb) can be used to bruteforce url IDS and find valid ones, so that past allocations can be found (I already did this for MIEIC up to 2019)
 * Additionally, [@antonioalmeida](https://github.com/antonioalmeida) has created a google sheets that is reusable for further years that allows for real-time updates if all students specify their preferences. The sheet can be copied from [here](https://docs.google.com/spreadsheets/d/1QpH6maW9Tb7YCyWM4nZzn4NqUqugzbuuKvaCqaqQONY/edit?usp=sharing).

## Previous MIEIC years
 * [12/13](https://sigarra.up.pt/feup/pt/coop_candidatura_geral.ver_colocacoes_aluno?pi_processo_view_id=1000861) - 1000861
 * [13/14](https://sigarra.up.pt/feup/pt/coop_candidatura_geral.ver_colocacoes_aluno?pi_processo_view_id=1002664) - 1002664
 * [14/15](https://sigarra.up.pt/feup/pt/coop_candidatura_geral.ver_colocacoes_aluno?pi_processo_view_id=1004742) - 1004742
 * [15/16](https://sigarra.up.pt/feup/pt/coop_candidatura_geral.ver_colocacoes_aluno?pi_processo_view_id=1006885) - 1006885
 * [16/17](https://sigarra.up.pt/feup/pt/coop_candidatura_geral.ver_colocacoes_aluno?pi_processo_view_id=1008349) - 1008349
 * [17/18](https://sigarra.up.pt/feup/pt/coop_candidatura_geral.ver_colocacoes_aluno?pi_processo_view_id=1010349) - 1010349
 * [18/19](https://sigarra.up.pt/feup/pt/coop_candidatura_geral.ver_colocacoes_aluno?pi_processo_view_id=1012045) - 1012045
 
## Legacy
This is probably a stationary repo, as far as my dedication goes, but...

Here are some ideas for people that might want to improve it:
 * Extend to other faculties (maybe even works by changing the URL)
 * Perform the scrapping using a cron job on future years and PR
