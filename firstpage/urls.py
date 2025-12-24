from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
    path('add-recommendation/', views.add_recommendation, name='add_recommendation'),
    path('motivation/', views.motivation, name='motivation'),


    path('programs/', views.programs, name='programs'),
    path('calculator/', views.calculator_view, name='calculator'),

path('programs/level1/', views.program_level1, name='program_level1'),
path('programs/level1/day1/', views.program_level1_day1, name='program_level1_day1'),
path('programs/level1/day2/', views.program_level1_day2, name='program_level1_day2'),
path('programs/level1/day3/', views.program_level1_day3, name='program_level1_day3'),



# Program 2
path('programs/level2/', views.program_level2, name='program_level2'),
path('programs/level2/day1/', views.program_level2_day1, name='program_level2_day1'),
path('programs/level2/day2/', views.program_level2_day2, name='program_level2_day2'),
path('programs/level2/day3/', views.program_level2_day3, name='program_level2_day3'),

# Program 3
path('programs/level3/', views.program_level3, name='program_level3'),
path('programs/level3/day1/', views.program_level3_day1, name='program_level3_day1'),
path('programs/level3/day2/', views.program_level3_day2, name='program_level3_day2'),
path('programs/level3/day3/', views.program_level3_day3, name='program_level3_day3'),

# Program 4
path('programs/level4/', views.program_level4, name='program_level4'),
path('programs/level4/day1/', views.program_level4_day1, name='program_level4_day1'),
path('programs/level4/day2/', views.program_level4_day2, name='program_level4_day2'),
path('programs/level4/day3/', views.program_level4_day3, name='program_level4_day3'),
path('programs/level4/day4/', views.program_level4_day4, name='program_level4_day4'),


# Program 5
path('programs/level5/', views.program_level5, name='program_level5'),
path('programs/level5/day1/', views.program_level5_day1, name='program_level5_day1'),
path('programs/level5/day2/', views.program_level5_day2, name='program_level5_day2'),
path('programs/level5/day3/', views.program_level5_day3, name='program_level5_day3'),
path('programs/level5/day4/', views.program_level5_day4, name='program_level5_day4'),


# Program 5 Lower focus
path('programs/level5_lower/', views.program_level5_lower, name='program_level5_lower'),
path('programs/level5_lower/day1/', views.program_level5_lower_day1, name='program_level5_lower_day1'),
path('programs/level5_lower/day2/', views.program_level5_lower_day2, name='program_level5_lower_day2'),
path('programs/level5_lower/day3/', views.program_level5_lower_day3, name='program_level5_lower_day3'),
path('programs/level5_lower/day4/', views.program_level5_lower_day4, name='program_level5_lower_day4'),


# Program 6
path('programs/level6/', views.program_level6, name='program_level6'),
path('programs/level6/day1/', views.program_level6_day1, name='program_level6_day1'),
path('programs/level6/day2/', views.program_level6_day2, name='program_level6_day2'),
path('programs/level6/day3/', views.program_level6_day3, name='program_level6_day3'),
path('programs/level6/day4/', views.program_level6_day4, name='program_level6_day4'),
path('programs/level6/day5/', views.program_level6_day5, name='program_level6_day5'),


# Program 6 Upper focus
path('programs/level6_upper/', views.program_level6_upper, name='program_level6_upper'),
path('programs/level6_upper/day1/', views.program_level6_upper_day1, name='program_level6_upper_day1'),
path('programs/level6_upper/day2/', views.program_level6_upper_day2, name='program_level6_upper_day2'),
path('programs/level6_upper/day3/', views.program_level6_upper_day3, name='program_level6_upper_day3'),
path('programs/level6_upper/day4/', views.program_level6_upper_day4, name='program_level6_upper_day4'),
path('programs/level6_upper/day5/', views.program_level6_upper_day5, name='program_level6_upper_day5'),


# Program 6 Lower focus
path('programs/level6_lower/', views.program_level6_lower, name='program_level6_lower'),
path('programs/level6_lower/day1/', views.program_level6_lower_day1, name='program_level6_lower_day1'),
path('programs/level6_lower/day2/', views.program_level6_lower_day2, name='program_level6_lower_day2'),
path('programs/level6_lower/day3/', views.program_level6_lower_day3, name='program_level6_lower_day3'),
path('programs/level6_lower/day4/', views.program_level6_lower_day4, name='program_level6_lower_day4'),
path('programs/level6_lower/day5/', views.program_level6_lower_day5, name='program_level6_lower_day5'),


# Program 9days Upper focus
path('programs/9days_upper/', views.program_9days_upper, name='program_9days_upper'),
path('programs/9days_upper/day1/', views.program_9days_upper_day1, name='program_9days_upper_day1'),
path('programs/9days_upper/day2/', views.program_9days_upper_day2, name='program_9days_upper_day2'),
path('programs/9days_upper/day3/', views.program_9days_upper_day3, name='program_9days_upper_day3'),
path('programs/9days_upper/day5/', views.program_9days_upper_day5, name='program_9days_upper_day5'),
path('programs/9days_upper/day6/', views.program_9days_upper_day6, name='program_9days_upper_day6'),
path('programs/9days_upper/day7/', views.program_9days_upper_day7, name='program_9days_upper_day7'),




# Program 9days Lower focus
path('programs/9days_lower/', views.program_9days_lower, name='program_9days_lower'),
path('programs/9days_lower/day1/', views.program_9days_lower_day1, name='program_9days_lower_day1'),
path('programs/9days_lower/day2/', views.program_9days_lower_day2, name='program_9days_lower_day2'),
path('programs/9days_lower/day3/', views.program_9days_lower_day3, name='program_9days_lower_day3'),
path('programs/9days_lower/day5/', views.program_9days_lower_day5, name='program_9days_lower_day5'),
path('programs/9days_lower/day6/', views.program_9days_lower_day6, name='program_9days_lower_day6'),
path('programs/9days_lower/day7/', views.program_9days_lower_day7, name='program_9days_lower_day7'),



#Program 15days Bench press focus
path('programs/15days_bench_press/', views.program_15days_bench_press, name='program_15days_bench_press'),
path('programs/15days_bench_press/day1/', views.program_15days_bench_press_day1, name='program_15days_bench_press_day1'),
path('programs/15days_bench_press/day2/', views.program_15days_bench_press_day2, name='program_15days_bench_press_day2'),
path('programs/15days_bench_press/day3/', views.program_15days_bench_press_day3, name='program_15days_bench_press_day3'),
path('programs/15days_bench_press/day6/', views.program_15days_bench_press_day6, name='program_15days_bench_press_day6'),
path('programs/15days_bench_press/day7/', views.program_15days_bench_press_day7, name='program_15days_bench_press_day7'),
path('programs/15days_bench_press/day8/', views.program_15days_bench_press_day8, name='program_15days_bench_press_day8'),
path('programs/15days_bench_press/day11/', views.program_15days_bench_press_day11, name='program_15days_bench_press_day11'),
path('programs/15days_bench_press/day12/', views.program_15days_bench_press_day12, name='program_15days_bench_press_day12'),
path('programs/15days_bench_press/day13/', views.program_15days_bench_press_day13, name='program_15days_bench_press_day13'),



]