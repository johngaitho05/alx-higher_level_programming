#include <Python.h>
#include <stdio.h>

#define custom_pybtes_as_string(op) (((PyBytesObject *)(op))->ob_sval)
#define custom_pyfloat_as_double(op) (((PyFloatObject *)(op))->ob_fval)
#define custom_pybytes_get_size(op) (((PyVarObject *)(op))->ob_size)
#define custom_pylist_size(op) (((PyVarObject *)(op))->ob_size)

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
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}
	setbuf(stdout, NULL);
	printf("  size: %zd\n", custom_pybytes_get_size(p));
	printf("  trying string: %s\n", custom_pybtes_as_string(p));
	printf("  first %zd bytes: ", custom_pybytes_get_size(p) + 1);
	if (custom_pybytes_get_size(p) >= 10)
	{
		for (int i = 0; i < 10; ++i)
			printf("%02hhx ", *((char *) (custom_pybtes_as_string(p)) + i));
	} else
	{
		for (Py_ssize_t i = 0; i <= custom_pybytes_get_size(p); ++i)
			printf("%02hhx ", *((char *) (custom_pybtes_as_string(p)) + i));
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: A pointer to the PyObject representing the float object
 */
void print_python_float(PyObject *p)
{
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Float Object\n");
		return;
	}
	double value = custom_pyfloat_as_double(p);

	char buffer[100];

	snprintf(buffer, sizeof(buffer), "%.15f", value);

	size_t length = strlen(buffer);

	while (length > 2 && buffer[length - 1] == '0')
	{
		if (buffer[length - 2] == '.')
			break;
		buffer[--length] = '\0';
	}

	if (buffer[length - 1] == '.')
		strcat(buffer, "0");

	printf("  value: %s\n", buffer);
}


/**
 * print_python_list - Prints information about a Python list object
 * @p: A pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = custom_pylist_size(p);

	setbuf(stdout, NULL);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *) p)->allocated);
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = retrieve_item(p, i);

		printf("Element %zd: %s\n", i, custom_py_type(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}
