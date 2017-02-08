cat <( sed -n '1,/SESSIONS/p' ../tsung/tsung.template.xml) \
	<( python scenario.py ) \
	<( sed -n '/SESSIONS/,$p' ../tsung/tsung.template.xml) \
	> ../tsung/tsung.xml
