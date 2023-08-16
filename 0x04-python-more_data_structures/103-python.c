#include <Python.h>
#include <stdio.h>

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
			PyObject *item = PyList_GetItem(p, i);

			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "Invalid Python List Object\n");
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: A pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		char *bytes = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
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
		fprintf(stderr, "Invalid Bytes Object\n");
	}
}
