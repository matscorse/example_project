import numpy as np 
import dask.array as da
import xarray as xr
import warnings
warnings.filterwarnings('ignore')
##xr.set_options(display_expand_data=False);

# -- numpy array 
sst_np = np.random.rand(300,450)
type(sst_np)

sst_da = da.from_array( sst_np)
print(sst_da)

# similarly we can convert them to xarray datarray
sst_xr = xr.DataArray(sst_da)
print(sst_xr)

# we can add dimension names to this:
sst_xr = xr.DataArray(sst_da,dims=['lat','lon'])

print(sst_xr.dims)

# -- create some dummy values for lat and lon dimensions
lat = np.random.uniform(low=-90, high=90, size=300)
lon = np.random.uniform(low=-180, high=180, size=450)

sst_xr = xr.DataArray(sst_da,
                      dims=['lat','lon'],
                      coords={'lat': lat, 'lon':lon},
                      attrs=dict(
                        description="Sea Surface Temperature.",
                        units="degC")
                     )
print(sst_xr)
