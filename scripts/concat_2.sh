cat <( sed -n '1,/SESSIONS/p' ../tsung_2/tsung.template.xml) \
	<( python scenario_2.py ) \
	<( sed -n '/SESSIONS/,$p' ../tsung_2/tsung.template.xml) \
	> ../tsung_2/tsung.xml
