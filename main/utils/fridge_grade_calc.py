from main.models import Fridge, FridgeGrade


def calc_grade():
    fridges = Fridge.objects.all()
    for f in fridges:
        grade = FridgeGrade.objects.create(fridge_id=f.pk)
        f.save()
        comments = f.fridgecomment_set.all()
        for comm in comments:
            if comm.grade == 0:
                grade.total_grade += 5
                grade.neutral_count += 1
            elif comm.grade == 1:
                grade.total_grade += 10
                grade.positive_count += 1
            elif comm.grade == 2:
                grade.total_grade -= 10
                grade.negative_count += 1
        grade.save()
        f.fridgegrade = grade
        f.save()


calc_grade()
