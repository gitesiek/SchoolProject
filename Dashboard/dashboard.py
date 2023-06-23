from flask import Blueprint, render_template
from flask_login import login_required
from Dashboard.analysis import (
    perform_trend_analysis,
    perform_seasonal_analysis,
    perform_summary_statistics,
    perform_predictive_analysis
)


dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard_bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard/main.html')



@dashboard_bp.route('/trend_analysis')
@login_required
def trend_analysis():
    trend_plot_data = perform_trend_analysis()
    return render_template('dashboard/analysis.html', trend_plot_data=trend_plot_data)

@dashboard_bp.route('/seasonal_analysis')
@login_required
def seasonal_analysis():
    seasonal_plot_data = perform_seasonal_analysis()
    return render_template('dashboard/analysis.html', trend_plot_data=seasonal_plot_data)

@dashboard_bp.route('/summary_statistics')
@login_required
def summary_statistics():
    summary_data = perform_summary_statistics()
    return render_template('dashboard/summary.html', table5_stats=summary_data)

@dashboard_bp.route('/predictive_analysis')
@login_required
def predictive_analysis():
    predicted_wages = perform_predictive_analysis()
    return render_template('dashboard/predictive.html', predicted_wages=predicted_wages)
