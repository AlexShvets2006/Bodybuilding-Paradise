from django.shortcuts import render

from .models import Recommendation



def recommendations_view(request):
    recommendations = Recommendation.objects.all().order_by('-created_at')
    return render(
        request,
        'pagefirst/recommendations.html',
        {'recommendations': recommendations}
    )




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Recommendation
import json


@csrf_exempt
def add_recommendation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            title = data.get("title")
            content = data.get("content")
            author = data.get("author", "Anonymous")

            if not title or not content:
                return JsonResponse(
                    {"error": "Title and content are required"},
                    status=400
                )

            rec = Recommendation.objects.create(
                title=title,
                content=content,
                author=author
            )

            return JsonResponse({
                "id": rec.id,
                "title": rec.title,
                "content": rec.content,
                "author": rec.author,
                "created_at": rec.created_at.strftime("%Y-%m-%d %H:%M")
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=405)





def index(request):
    return render(request, 'pagefirst/index.html')

def about(request):
    return render(request, 'pagefirst/about.html')

def motivation(request):
    return render(request, 'pagefirst/motivation.html')



def programs(request):
    return render(request, 'pagefirst/programs.html')
def calculator(request):
    return render(request, 'pagefirst/calculator.html')


def program_level1(request):
    return render(request, 'pagefirst/program_level1.html')
def program_level1_day1(request):
    return render(request, 'pagefirst/level1_day1.html')
def program_level1_day2(request):
    return render(request, 'pagefirst/level1_day2.html')
def program_level1_day3(request):
    return render(request, 'pagefirst/level1_day3.html')



def program_level2(request):
    return render(request, 'pagefirst/program_level2.html')
def program_level2_day1(request):
    return render(request, 'pagefirst/level2_day1.html')
def program_level2_day2(request):
    return render(request, 'pagefirst/level2_day2.html')
def program_level2_day3(request):
    return render(request, 'pagefirst/level2_day3.html')



def program_level3(request):
    return render(request, 'pagefirst/program_level3.html')
def program_level3_day1(request):
    return render(request, 'pagefirst/level3_day1.html')
def program_level3_day2(request):
    return render(request, 'pagefirst/level3_day2.html')
def program_level3_day3(request):
    return render(request, 'pagefirst/level3_day3.html')




def program_level4(request):
    return render(request, 'pagefirst/program_level4.html')
def program_level4_day1(request):
    return render(request, 'pagefirst/level4_day1.html')
def program_level4_day2(request):
    return render(request, 'pagefirst/level4_day2.html')
def program_level4_day3(request):
    return render(request, 'pagefirst/level4_day3.html')
def program_level4_day4(request):
    return render(request, 'pagefirst/level4_day4.html')



def program_level5(request):
    return render(request, 'pagefirst/program_level5.html')
def program_level5_day1(request):
    return render(request, 'pagefirst/level5_day1.html')
def program_level5_day2(request):
    return render(request, 'pagefirst/level5_day2.html')
def program_level5_day3(request):
    return render(request, 'pagefirst/level5_day3.html')
def program_level5_day4(request):
    return render(request, 'pagefirst/level5_day4.html')



def program_level5_lower(request):
    return render(request, 'pagefirst/program_level5_lower.html')
def program_level5_lower_day1(request):
    return render(request, 'pagefirst/level5_lower_day1.html')
def program_level5_lower_day2(request):
    return render(request, 'pagefirst/level5_lower_day2.html')
def program_level5_lower_day3(request):
    return render(request, 'pagefirst/level5_lower_day3.html')
def program_level5_lower_day4(request):
    return render(request, 'pagefirst/level5_lower_day4.html')


def program_level6(request):
    return render(request, 'pagefirst/program_level6.html')
def program_level6_day1(request):
    return render(request, 'pagefirst/level6_day1.html')
def program_level6_day2(request):
    return render(request, 'pagefirst/level6_day2.html')
def program_level6_day3(request):
    return render(request, 'pagefirst/level6_day3.html')
def program_level6_day4(request):
    return render(request, 'pagefirst/level6_day4.html')
def program_level6_day5(request):
    return render(request, 'pagefirst/level6_day5.html')


def program_level6_upper(request):
    return render(request, 'pagefirst/program_level6_upper.html')
def program_level6_upper_day1(request):
    return render(request, 'pagefirst/level6_upper_day1.html')
def program_level6_upper_day2(request):
    return render(request, 'pagefirst/level6_upper_day2.html')
def program_level6_upper_day3(request):
    return render(request, 'pagefirst/level6_upper_day3.html')
def program_level6_upper_day4(request):
    return render(request, 'pagefirst/level6_upper_day4.html')
def program_level6_upper_day5(request):
    return render(request, 'pagefirst/level6_upper_day5.html')




def program_level6_lower(request):
    return render(request, 'pagefirst/program_level6_lower.html')
def program_level6_lower_day1(request):
    return render(request, 'pagefirst/level6_lower_day1.html')
def program_level6_lower_day2(request):
    return render(request, 'pagefirst/level6_lower_day2.html')
def program_level6_lower_day3(request):
    return render(request, 'pagefirst/level6_lower_day3.html')
def program_level6_lower_day4(request):
    return render(request, 'pagefirst/level6_lower_day4.html')
def program_level6_lower_day5(request):
    return render(request, 'pagefirst/level6_lower_day5.html')



def program_9days_upper(request):
    return render(request, 'pagefirst/program_9days_upper.html')
def program_9days_upper_day1(request):
    return render(request, 'pagefirst/9days_upper_day1.html')
def program_9days_upper_day2(request):
    return render(request, 'pagefirst/9days_upper_day2.html')
def program_9days_upper_day3(request):
    return render(request, 'pagefirst/9days_upper_day3.html')
def program_9days_upper_day5(request):
    return render(request, 'pagefirst/9days_upper_day5.html')
def program_9days_upper_day6(request):
    return render(request, 'pagefirst/9days_upper_day6.html')
def program_9days_upper_day7(request):
    return render(request, 'pagefirst/9days_upper_day7.html')


def program_9days_lower(request):
    return render(request, 'pagefirst/program_9days_lower.html')
def program_9days_lower_day1(request):
    return render(request, 'pagefirst/9days_lower_day1.html')
def program_9days_lower_day2(request):
    return render(request, 'pagefirst/9days_lower_day2.html')
def program_9days_lower_day3(request):
    return render(request, 'pagefirst/9days_lower_day3.html')
def program_9days_lower_day5(request):
    return render(request, 'pagefirst/9days_lower_day5.html')
def program_9days_lower_day6(request):
    return render(request, 'pagefirst/9days_lower_day6.html')
def program_9days_lower_day7(request):
    return render(request, 'pagefirst/9days_lower_day7.html')




def program_15days_bench_press(request):
    return render(request, 'pagefirst/program_15days_bench_press.html')
def program_15days_bench_press_day1(request):
    return render(request, 'pagefirst/15days_bench_press_day1.html')
def program_15days_bench_press_day2(request):
    return render(request, 'pagefirst/15days_bench_press_day2.html')
def program_15days_bench_press_day3(request):
    return render(request, 'pagefirst/15days_bench_press_day3.html')
def program_15days_bench_press_day6(request):
    return render(request, 'pagefirst/15days_bench_press_day6.html')
def program_15days_bench_press_day7(request):
    return render(request, 'pagefirst/15days_bench_press_day7.html')
def program_15days_bench_press_day8(request):
    return render(request, 'pagefirst/15days_bench_press_day8.html')
def program_15days_bench_press_day11(request):
    return render(request, 'pagefirst/15days_bench_press_day11.html')
def program_15days_bench_press_day12(request):
    return render(request, 'pagefirst/15days_bench_press_day12.html')
def program_15days_bench_press_day13(request):
    return render(request, 'pagefirst/15days_bench_press_day13.html')








from django.http import JsonResponse
from django.shortcuts import render

def calculator_view(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        height = float(request.POST.get("height"))
        weight = float(request.POST.get("weight"))
        age = float(request.POST.get("age"))
        sex = request.POST.get("sex")
        activity = float(request.POST.get("activity"))
        goal = request.POST.get("goal")

        # === BMR ===
        if sex == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        # === TDEE ===
        tdee = bmr * activity

        # === Target calories based on goal ===
        if goal == "cut":
            target = tdee * 0.9
        elif goal == "maintain":
            target = tdee
        elif goal == "bulk":
            target = tdee * 1.1

        # === Protein ratios ===
        protein_ratios = {
            "male":     {"cut": 2.0, "maintain": 1.6, "bulk": 1.8},
            "female":   {"cut": 1.7, "maintain": 1.3, "bulk": 1.6},
        }

        # === Fat ratios ===
        fat_ratios = {
            "male":     {"cut": 0.7, "maintain": 1.1, "bulk": 1.4},
            "female":   {"cut": 0.6, "maintain": 1.0, "bulk": 1.2},
        }

        # === Protein grams per day ===
        protein = weight * protein_ratios[sex][goal]

        # === Fat grams per day ===
        fat = weight * fat_ratios[sex][goal]

        # === Carbs ===
        calories_from_protein = protein * 4
        calories_from_fat = fat * 9
        calories_from_carbs = target - (calories_from_protein + calories_from_fat)
        carbs = calories_from_carbs / 4

        return JsonResponse({
            "bmr": round(bmr),
            "tdee": round(tdee),
            "target_calories": round(target),
            "protein": round(protein),
            "fat": round(fat),
            "carbs": round(carbs),
        })

    return render(request, "pagefirst/calculator.html")








































































