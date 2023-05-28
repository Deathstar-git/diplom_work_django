from main.models import Multicooker, MulticookerGrade


def calc_grade():
    multicookers = Multicooker.objects.all()
    for c in multicookers:
        grade = MulticookerGrade.objects.create(multicooker_id=c.pk)
        c.save()
        comments = c.multicookercomment_set.all()
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
        c.multicookergrade = grade
        c.save()


calc_grade()
