from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, SavingsGoal
from .forms import IncomeForm, ExpenseForm, SavingsGoalForm

def dashboard(request):
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    savings_goals = SavingsGoal.objects.filter(user=request.user)
    context = {
        'incomes': incomes,
        'expenses': expenses,
        'savings_goals': savings_goals,
    }
    return render(request, 'tracker/dashboard.html', context)

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'tracker/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})

def add_savings_goal(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            savings_goal = form.save(commit=False)
            savings_goal.user = request.user
            savings_goal.save()
            return redirect('dashboard')
    else:
        form = SavingsGoalForm()
    return render(request, 'tracker/add_savings_goal.html', {'form': form})
