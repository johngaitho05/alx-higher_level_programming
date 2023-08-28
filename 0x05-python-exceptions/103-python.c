#include <Python.h>
#include <stdio.h>

#define bytes_to_str(op) (((PyBytesObject *)(op))->ob_sval)
#define float_to_double(op) (((PyFloatObject *)(op))->ob_fval)
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
	double value = float_to_double(p);

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
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: A pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		char *bytes = bytes_to_str(p);

		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", bytes);

		printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
		for (Py_ssize_t i = 0; i < size + 1 && i < 10; i++)
		{
			printf("%02hhx", bytes[i]);
			if (i < size)
				printf(" ");
		}
		printf("\n");
	} else
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Prints information about a Python list object.
 * @p: A pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		Py_ssize_t size = custom_pylist_size(p);

		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (Py_ssize_t i = 0; i < size; i++)
		{
			PyObject *item = retrieve_item(p, i);

			printf("Element %ld: %s\n", i, custom_py_type(item)->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			if (PyFloat_Check(item))
				print_python_float(item);
		}
	}
	else
	{
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
	}
}
