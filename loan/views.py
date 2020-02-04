from django.shortcuts import render
from django.contrib.auth.models import Loan


def apply_loan(request,name,phone,amount,rate,days):
    """It will create a field having user and loan details"""
    try:
        Loan.objects.create_user(name, phone,amount,rate,days)
        return True
    except:
        return None


def approve_loan(request, loan_id, approve=False):
    """Admin has to pass true to approve the loan"""
    try:
        if approve:
            ap = Loan.objects.get(id=loan_id)
            ap.approved = True  # modify approved to true
            ap.save()
            return True
        return False
    except:
        return None


def get_loan_applied_users(request):
    """Get list of all users applied for the loan"""
    return Loan.objects.all()


def get_non_approved_loans(request):
    """Get list of all users having non-approved loan"""
    return Loan.objects.filter(approved=False)

