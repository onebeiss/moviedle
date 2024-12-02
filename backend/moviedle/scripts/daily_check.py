#!/usr/bin/env python3

import calendar
from datetime import datetime
from updates_movies import update_movie_files

def should_run_update():
    today = datetime.now()
    _, last_day_of_month = calendar.monthrange(today.year, today.month)
    three_days_before_end = last_day_of_month - 3

    # Comprueba si es el día 3 días antes del fin de mes o el día 27 como fallback
    return today.day == three_days_before_end or today.day == 27

if __name__ == "__main__":
    if should_run_update():
        update_movie_files()
    else:
        print("\n·········································································")
        print("* No es el día de actualización mensual de películas")
        print("* La actualización está prevista para 3 días antes del final del mes.")
        print("·········································································\n")