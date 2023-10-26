
class NETCDF4.dataset(filename, mode='r', clobber=True, format='NETCDF4', diskless=False, persist=False, keepweakref=False, comm=None, info=None)
    """
    A class representing a netCDF dataset.

    Args:
    - filename (str or file-like object): The name of the netCDF file or an open file object.
    - mode (str): The file open mode, which can be 'r' (read-only), 'w' (write), 'a' (append), or 'r+' (read and write).
    - clobber (bool): If True and the file already exists, overwrite the existing file. If False and the file already exists, raise an exception.
    - format (str): The netCDF file format to use, which can be 'NETCDF3_CLASSIC', 'NETCDF3_64BIT_OFFSET', 'NETCDF3_64BIT_DATA', 'NETCDF4', or 'NETCDF4_CLASSIC'.
    - diskless (bool): If True, the netCDF file is created in memory instead of on disk.
    - persist (bool): If True, the netCDF file is kept in memory after the file is closed.
    - keepweakref (bool): If True, the Dimension and Variable child objects only hold weak references to the parent Dataset or Group.
    - comm (MPI communicator): An MPI communicator for creating parallel netCDF files.
    - info (object): Additional information object that can be passed to the underlying netCDF library.
   
    file: El nombre del archivo netCDF o un objeto de archivo abierto.
    mode: El modo de apertura del archivo, que puede ser 'r' (solo lectura), 'w' (escritura), 'a' (anexar), o 'r+' (lectura y escritura).
    clobber: Si es True y el archivo ya existe, sobrescribe el archivo existente. Si es False y el archivo ya existe, lanza una excepción.
    format: El formato de archivo netCDF que se utilizará, que puede ser 'NETCDF3_CLASSIC', 'NETCDF3_64BIT_OFFSET', 'NETCDF3_64BIT_DATA', 'NETCDF4', o 'NETCDF4_CLASSIC'.
    diskless: Si es True, el archivo netCDF se crea en la memoria en lugar de en el disco.
    persist: Si es True, el archivo netCDF se mantiene en la memoria después de que se cierra el archivo.
    keepweakref: Si es True, los objetos secundarios Dimensión y Variables solo mantienen referencias débiles al conjunto de datos o grupo principal.
    comm: Un comunicador MPI para la creación de archivos netCDF paralelos.
    info: Un objeto de información adicional que se puede pasar a la biblioteca subyacente de netCDF.
    
    Methods:
        - close(): Cierra el archivo netCDF.
        - sync(): Sincroniza el archivo netCDF con el disco.
        - createDimension(name, length): Crea una dimensión.
        - createVariable(name, datatype, dimensions): Crea una variable.
        - createGroup(name): Crea un grupo.
        - setncattr(name, value): Establece un atributo global.
        - __getitem__(key): Devuelve una variable o un grupo.
        - __setitem__(key, value): Establece una variable o un grupo.
        - __delitem__(key): Elimina una variable o un grupo.
        - __iter__(): Itera sobre las variables y grupos.
        - __contains__(key): Comprueba si una variable o un grupo está en el conjunto de datos.
        - __len__(): Devuelve el número de variables y grupos.
        - __enter__(): Devuelve el objeto Dataset.
        - __exit__(exc_type, exc_value, traceback): Cierra el archivo netCDF.
        - __str__(): Devuelve una representación de cadena del conjunto de datos.
        - __repr__(): Devuelve una representación de cadena del conjunto de datos.
        - __getattr__(name): Devuelve un atributo global.
        - __setattr__(name, value): Establece un atributo global.
        - __delattr__(name): Elimina un atributo global.
        - __dir__(): Devuelve una lista de atributos globales.
        - __copy__(): Crea una copia del conjunto de datos.
        - __deepcopy__(): Crea una copia profunda del conjunto de datos.
        - __eq__(other): Comprueba si el conjunto de datos es igual a otro.

            a
    
    """
