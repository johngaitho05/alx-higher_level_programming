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
 * This function is necessary to initialize
 * the module when it's imported in Python.
 * Return: a python object
 */
PyMODINIT_FUNC PyInit_libPyList(void)
{
	PyObject *module;

	static PyMethodDef methods[] = {
			{NULL, NULL, 0, NULL} /* Sentinel */
	};

	static struct PyModuleDef moduledef = {
			PyModuleDef_HEAD_INIT,
			"libPyList",  /* Name of the module */
			NULL,         /* Module documentation */
			/*
			 * Size of the per-interpreter state of the module,
			 * * or -1 if the module keeps state in global variables.
			 */
			-1,
			methods,      /* Method definitions */
			NULL,         /* Slot definitions */
			NULL,         /* Optional module-traverse function */
			NULL,         /* Optional clear function */
			NULL          /* Optional module destructor */
	};

	module = PyModule_Create(&moduledef);
	if (module == NULL)
	{
		return (NULL);
	}

	return (module);
}
