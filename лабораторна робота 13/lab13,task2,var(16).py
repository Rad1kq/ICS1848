from journal import JOURNAL


journal_1 = JOURNAL(
    "Наука і життя", "Освіта", "Україна", "ТОВ «Освіта»", 1, 2026
)
journal_1.AddPaper("Нові відкриття в науці")
journal_1.AddPaper("Сучасні технології")

journal_2 = JOURNAL(
    "Світ подорожей", "Мандрівник", "Україна", "ПП «Мандрівник»", 2, 2026
)
journal_2.AddPaper("Найкращі місця Європи")
journal_2.AddPaper("Подорожі без зайвих витрат")
journal_2.AddPaper("Історія стародавніх міст")

journal_3 = JOURNAL(
    "Спорт сьогодні", "Олімп", "Україна", "Видавництво «Олімп»", 3, 2026
)
journal_3.AddPaper("Підготовка до змагань")
journal_3.AddPaper("Здоровий спосіб життя")


for journal in (journal_1, journal_2, journal_3):
    print("\n" + "=" * 40)
    journal.DisplayProperties()
    journal.DisplayPapers()
