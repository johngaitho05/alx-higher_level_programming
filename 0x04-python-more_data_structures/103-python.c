#include <Python.h>

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

		printf("  [.] size: %ld\n", size);
		printf("  [.] trying string: %s\n", bytes);

		printf("  [.] first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
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
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);

		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (Py_ssize_t i = 0; i < size; i++)
		{
			PyObject *item = retrieve_item(p, i);

			printf("Element %ld: %s\n", i, custom_py_type(item)->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
		}
	}
	else
	{
		fprintf(stderr, "Invalid Python List Object\n");
	}
}

