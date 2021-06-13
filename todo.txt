-> Resume Parser (2 functions- pdf/doc/txt; folder- all resume)
	Name,skills, working exp/internship ---- csv  (PARSER.PY)
-> Work experience sumamrise and keywords  (SUMMARY.PY)
-> Knowledge Graph Change (GRAPH.PY)
-> Job Recommendation Model (MODEL.PY)

data.csv
	name - Name string
	phone - Phone string
	address - Address string
	skills - Array of skills
	workExp - paragraph

clean_data.csv (added cols) - created by dataCleaning.py
	processed_workExp - processed work experience

summary_data.csv (added cols) - created by summary.py
	summary - summarised processed_workExp
	keywords - keywords from projects (array)