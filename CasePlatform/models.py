from django.db import models

from service.models import User
# Create your models here.




class INP_CASE_META(models.Model):
    Row_id = models.AutoField(primary_key=True)
    Meta_id = models.CharField(max_length=100, null=False, blank=False)
    case_type = models.CharField(max_length=100, null=False, blank=False)
    issue_code = models.CharField(max_length=100, null=False, blank=False)
    issue_detail = models.TextField(null=False, blank=False)
    Parent=models.CharField(max_length=100, null=True, blank=True)
    priority = models.CharField(max_length=100, null=False, blank=False)
    sla_hours = models.IntegerField(null=False, blank=False)
    ticket_type = models.CharField(max_length=100, null=False, blank=False)
    sub_type = models.CharField(max_length=100, null=False, blank=False)
    sub_sub_type = models.CharField(max_length=100, null=False, blank=False)
    rule_id = models.CharField(max_length=100, null=False, blank=False)
    rule_version = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Meta_id)




# inp_case_meta
# --------------------------------------------------
# id
# lob
# case_type
# ticket_type
# sub_type
# sub_sub_type
# issue_code
# issue_detail
# priority
# sla_hours
# rule_id
# rule_version
# is_active
# created_at
# updated_at


class INP_CASE(models.Model):
    Row_id = models.AutoField(primary_key=True)
    meta_id = models.ForeignKey(INP_CASE_META, on_delete=models.CASCADE, null=False, blank=False)
    customer_id = models.CharField(max_length=15, null=False, blank=False) # Assuming you have a phone field in your User model
    lob = models.CharField(max_length=100, null=False, blank=False)
    Ticket_type = models.CharField(max_length=100, default='TT')
    sub_type = models.CharField(max_length=100, default='ST')
    sub_sub_type = models.CharField(max_length=100, default='SST')
    case_type = models.CharField(max_length=100, null=False, blank=False)
    issue_code = models.CharField(max_length=100, null=False, blank=False)
    issue_detail = models.TextField(null=False, blank=False)
    priority = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=100, null=False, blank=False)
    source = models.CharField(max_length=100, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_cases', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_cases', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.case_id)


# inp_case
# ---------------------------------------------
# id
# case_id
# customer_id : Mobile number of the customer
# lob
# case_type
# issue_code
# issue_detail
# priority
# status
# source
# created_by
# created_at
# updated_by
# updated_at




class INP_MILESTONE(models.Model):
    Row_id = models.AutoField(primary_key=True)
    milestone_id = models.CharField(max_length=100, null=False, blank=False)
    case_id = models.ForeignKey(INP_CASE, on_delete=models.CASCADE, null=False, blank=False)
    milestone_name = models.CharField(max_length=100, null=False, blank=False)
    milestone_status = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.milestone_id)





