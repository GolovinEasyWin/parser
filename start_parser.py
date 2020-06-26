# ©LG PolyRec, Peter the Great Polytechnical University, IBKS, 2020
# Developer: @GolovinEasyWin

import settings as st
import parse_functions as pf

# Формируем адрес для парсинга, опираясь на аргументы КС
URL = st.create_url(st.arg1)

# Запускаем парсинг сайта
pf.parse(URL)
