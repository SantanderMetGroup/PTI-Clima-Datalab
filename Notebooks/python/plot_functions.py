import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np

def plot_map(ds, var, function='climatology', measure='', first_period=None, last_period=None):
    '''
    This function plots either the climatology (mean) or the difference between two periods for a given variable.
    
    Parameters:
    - ds: xarray.Dataset with the data
    - function: 'climatology' for the mean over time or 'difference' for period-based difference
    - measure: 'rel' for relative difference (used only with 'difference')
    - var: The variable to plot
    - first_period: Tuple with the start and end year of the first period for difference calculation
    - last_period: Tuple with the start and end year of the second period for difference calculation
    '''
    #create the figure fix the rest so it works
    proj = ccrs.PlateCarree()
    
    # Number of models for subplots
    models = ds['model'].values if 'model' in ds.dims else [None]
    fig, axes = plt.subplots(1, len(models), figsize=(15, 6), subplot_kw={'projection': proj})
    axes = np.atleast_1d(axes)  # Handle single model case

    # Select the variable (replace 'variable_name' with actual variable)
    ds = ds[var]
    
    vmin, vmax = None, None

    # Iterate through the models to compute the results and determine global min and max
    for i, model in enumerate(models):
        ax = axes[i]
        data = ds.sel(model=model) if model else ds
        
        if function == 'climatology':
            result = data.mean(dim='time')
        elif function == 'difference' and first_period and last_period:
            data_first = data.sel(time=slice(first_period[0], first_period[1]))
            data_last = data.sel(time=slice(last_period[0], last_period[1]))
            result = data_last.mean(dim='time') - data_first.mean(dim='time')
            
            if measure == 'rel':
                result = (result / data_first.mean(dim='time')) * 100


        # Update global vmin and vmax
        if vmin is None or result.min() < vmin:
            vmin = result.min().values
        if vmax is None or result.max().values > vmax:
            vmax = result.max().values

    if vmax > vmin:
        vmin = - abs(vmax)
    else:
        vmax = abs(vmin)
    
    for i, model in enumerate(models):
        ax = axes[i]
        data = ds.sel(model=model) if model else ds
        
        if function == 'climatology':
            result = data.mean(dim='time')
        elif function == 'difference' and first_period and last_period:
            data_first = data.sel(time=slice(first_period[0], first_period[1]))
            data_last = data.sel(time=slice(last_period[0], last_period[1]))
            result = data_last.mean(dim='time') - data_first.mean(dim='time')
            
            if measure == 'rel':
                result = (result / data_first.mean(dim='time')) * 100
        
        # Plotting
        result.plot(ax=ax, transform=ccrs.PlateCarree(),cmap = 'coolwarm', vmax = vmax, vmin =vmin)
        ax.coastlines()
        title = f'{function.capitalize()} - {model}' if model else function.capitalize()
        ax.set_title(f'{title} ({measure} difference)' if measure else title)

    plt.tight_layout()
    plt.show()
    
    return fig

def plot_time_series(ds, var, function='climatology', measure='', period = None):
    '''
    Plots a time series with each line representing a model for a given variable.
    
    Parameters:
    - ds: xarray.Dataset containing the data with a 'model' dimension
    - var: The variable to plot
    - function: 'climatology' for the mean over time or 'difference' for period-based difference
    - measure: 'rel' for relative difference (used only with 'difference')
    - period: Tuple with the start and end year of the first period for difference calculation
    '''
    # Initialize the figure
    fig = plt.figure(figsize=(12, 6))
    
    # Check for 'model' dimension in dataset
    models = ds['model'].values if 'model' in ds.dims else [None]
    
    # Loop through each model and plot the time series
    for model in models:
        data = ds.sel(model=model)[var] if model else ds[var]
        time_series = data.mean(dim=('lat', 'lon'), skipna=True).resample(time='1YE').mean(dim='time')  # Spatial mean for each time point
        if function == 'climatology':
            results = time_series
        elif function == 'difference' and period:
            base_period_mean = time_series.sel(time=slice(period[0], period[1])).mean(dim='time')
            results = time_series - base_period_mean.values
            if measure == 'rel':
                results = (results / base_period_mean.values) * 100
                
        label = f'Model: {model}' if model else 'Data'
        plt.plot(results['time'], results, label=label)

    
    # Customizing the plot
    plt.xlabel('Time')
    if measure == 'rel':
        plt.ylabel('%')
    else:
        plt.ylabel(var)
    plt.title(f'{function.capitalize()} {measure.capitalize()}- Time Series of {var} by Model')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return fig

def plot_annual_cicle(ds, var, function='climatology', measure='', period = None):
    '''
    Plots a annual cicle with each line representing a model for a given variable.
    
    Parameters:
    - ds: xarray.Dataset containing the data with a 'model' dimension
    - var: The variable to plot
    - function: 'climatology' for the mean over time or 'difference' for period-based difference
    - measure: 'rel' for relative difference (used only with 'difference')
    - period: Tuple with the start and end year of the first period for difference calculation
    '''
    # Initialize the figure
    fig = plt.figure(figsize=(12, 6))
    
    # Check for 'model' dimension in dataset
    models = ds['model'].values if 'model' in ds.dims else [None]
    
    # Loop through each model and plot the time series
    for model in models:
        data = ds.sel(model=model)[var] if model else ds[var]
        time_series = data.mean(dim=('lat', 'lon'), skipna=True)

        # Group by month and compute the mean across all years
        monthly_mean = time_series.groupby('time.month').mean()
        if function == 'climatology':
            results = monthly_mean
        elif function == 'difference' and period:
            base_period_mean = time_series.sel(time=slice(period[0], period[1])).groupby('time.month').mean()
            results = monthly_mean - base_period_mean
            if measure == 'rel':
                results = (monthly_mean / base_period_mean) * 100
                
        label = f'Model: {model}' if model else 'Data'
        plt.plot(results['month'], results, label=label)

    
    # Customizing the plot
    plt.xlabel('Time')
    if measure == 'rel':
        plt.ylabel('%')
    else:
        plt.ylabel(var)
    plt.title(f'{function.capitalize()} {measure.capitalize()}- Annual Cicle of {var} by Model')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return fig