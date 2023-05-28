from main.models import MobilePhone, MobilePhoneGrade


def calc_grade():
    phones = MobilePhone.objects.all()
    for p in phones:
        grade = MobilePhoneGrade.objects.create(phone_id=p.pk)
        p.save()
        comments = p.mobilephonecomment_set.all()
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
        p.mobilephonegrade = grade
        p.save()


calc_grade()
