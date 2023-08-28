#include <Python.h>
#include <stdio.h>

#define bytes_to_str(op) (((PyBytesObject *)(op))->ob_sval)

static inline PyTypeObject *custom_py_type(PyObject *ob)
{
return (ob->ob_type);
}

/**
 * retrieve_item - Function to retrieve
 * an item from a Python list at a given index
 * @op: the list object
 * @i: index
 * Return: object at the given index
 */
PyObject *retrieve_item(PyObject *op, Py_ssize_t i)
{
	if (!PyList_Check(op))
	{
		PyErr_SetString(PyExc_TypeError, "Expected a list object");
		return (NULL);
	}

	PyListObject *list = (PyListObject *)op;
	Py_ssize_t size = list->ob_base.ob_size;

	if (i < 0 || i >= size)
	{
		PyErr_SetString(PyExc_IndexError, "List index out of range");
		return (NULL);
	}

	PyObject *item = list->ob_item[i];

	Py_INCREF(item);

	return (item);
}

/**
 * print_python_list - Prints information about a Python list object
 * @p: A pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *) p)->allocated);
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = retrieve_item(p, i);

		printf("Element %zd: %s\n", i, custom_py_type(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyBytesObject\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", PyBytes_GET_SIZE(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %zd bytes: ", PyBytes_GET_SIZE(p) + 1);
	if (PyBytes_GET_SIZE(p) >= 10)
	{
		for (int i = 0; i < 10; ++i)
			printf("%02hhx ", *((char *) (bytes_to_str(p)) + i));
	} else
	{
		for (Py_ssize_t i = 0; i <= PyBytes_GET_SIZE(p); ++i)
			printf("%02hhx ", *((char *) (bytes_to_str(p)) + i));
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: A pointer to the PyObject representing the float object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyFloatObject\n");
		return;
	}

	double value = PyFloat_AS_DOUBLE(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
