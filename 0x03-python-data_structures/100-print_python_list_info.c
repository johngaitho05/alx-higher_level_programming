#include <Python.h>

/**
 * print_python_list_info - interacts with python list object
 * @pList: python list object
 */
void print_python_list_info(PyObject *pList)
{
	Py_ssize_t size = PyList_Size(pList);
	Py_ssize_t allocated = ((PyListObject *)pList)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *pItem = PyList_GetItem(pList, i);
		const char *typeName = Py_TYPE(pItem)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 * PyInit_libPyList - python module
 * Return: a python object
 */
PyMODINIT_FUNC PyInit_libPyList(void)
{
	PyObject *module;

	static PyMethodDef methods[] = {
					{NULL, NULL, 0, NULL}
			};

	module = PyModule_Create(&moduledef);
	if (module == NULL)
	{
		return (NULL);
	}

	return (module);
}
