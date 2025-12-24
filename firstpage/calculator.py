# calculator_logic

class CalorieCalculator:
    """
    Класс для расчета калорий и макронутриентов на основе данных пользователя.
    Использует формулу Mifflin-St Jeor и гибкие настройки для БЖУ.
    """

    # Константы для калорийности макронутриентов
    CALORIES_PER_GRAM_PROTEIN = 4
    CALORIES_PER_GRAM_CARBS = 4
    CALORIES_PER_GRAM_FAT = 9

    def __init__(self, weight, height, age, sex, activity, goal):
        """
        Инициализация калькулятора с данными пользователя.
        """
        # Преобразуем входные данные в правильные типы для расчетов
        self.weight = float(weight)
        self.height = float(height)
        self.age = int(age)
        self.gender = gender  # 'male' or 'female'
        self.activity_level = float(activity_level)  # 1.2, 1.375, etc.
        self.goal = goal  # 'cut', 'maintain', 'bulk'

    def _calculate_bmr(self):
        """
        Расчет базового метаболизма (BMR) по формуле Mifflin-St Jeor.
        BMR - Basal Metabolic Rate.
        """
        if self.gender == 'male':
            # BMR = 10 * вес + 6.25 * рост – 5 * возраст + 5
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.gender == 'female':
            # BMR = 10 * вес + 6.25 * рост – 5 * возраст – 161
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        else:
            raise ValueError("Неверно указан пол. Используйте 'male' или 'female'.")

        return bmr

    def _calculate_tdee(self, bmr):
        """
        Расчет суточной потребности в калориях с учетом активности (TDEE).
        TDEE - Total Daily Energy Expenditure.
        """
        # TDEE = BMR × activity
        return bmr * self.activity_level

    def _calculate_target_calories(self, tdee):
        """
        Корректировка калорий в зависимости от цели.
        """
        if self.goal == 'cut':
            # Похудение: −20% калорий
            return tdee * 0.8
        elif self.goal == 'maintain':
            # Поддержание веса
            return tdee
        elif self.goal == 'bulk':
            # Набор массы: +5%
            return tdee * 1.10
        else:
            raise ValueError("Неверно указана цель. Используйте 'cut', 'maintain' или 'bulk'.")

    def _calculate_macros(self, target_calories):
        """
        Расчет макронутриентов (БЖУ) на основе цели и пола.
        """
        # Задаем коэффициенты для белков и жиров (грамм на кг веса)
        # Это делает код чище, чем длинные if/else конструкции
        protein_ratios = {
            'male': { 'cut' : 2.0, 'maintain' : 1.6, 'bulk' : 1.8 },
            'female': { 'cut' : 1.7, 'maintain' : 1.4 , 'bulk' : 1.6 },
        }
        fat_ratios = {
            'male': {'cut': 0.7, 'maintain': 1.1, 'bulk': 1.4},
            'female': {'cut': 1.0, 'maintain': 1.3, 'bulk': 1.5}  # Упрощаем для женщин, 0.8-1 -> 1.0
        }

        protein_g_per_kg = protein_ratios[self.gender][self.goal]
        fat_g_per_kg = fat_ratios[self.gender][self.goal]

        # 1. Считаем граммы белков и жиров
        protein_grams = self.weight * protein_g_per_kg
        fat_grams = self.weight * fat_g_per_kg

        # 2. Считаем калории от белков и жиров
        calories_from_protein = protein_grams * self.CALORIES_PER_GRAM_PROTEIN
        calories_from_fat = fat_grams * self.CALORIES_PER_GRAM_FAT

        # 3. Считаем углеводы из оставшихся калорий
        remaining_calories = target_calories - calories_from_protein - calories_from_fat
        carbs_grams = remaining_calories / self.CALORIES_PER_GRAM_CARBS

        # Убедимся, что углеводы не ушли в минус (если выбраны слишком высокие коэф. для Б и Ж)
        if carbs_grams < 0:
            carbs_grams = 0

        return {
            'protein': round(protein_grams),
            'fat': round(fat_grams),
            'carbs': round(carbs_grams)
        }

    def calculate_all(self):
        """
        Основной метод, который выполняет все расчеты по шагам и возвращает результат.
        """
        bmr = self._calculate_bmr()
        tdee = self._calculate_tdee(bmr)
        target_calories = self._calculate_target_calories(tdee)
        macros = self._calculate_macros(target_calories)

        return {
            'bmr': round(bmr),
            'tdee': round(tdee),
            'target_calories': round(target_calories),
            'protein': macros['protein'],
            'fat': macros['fat'],
            'carbs': macros['carbs']
        }




