#include "Python.h"
#include <stdio.h>

/**
 * print_python_bytes - Prints the number of bytes of a byte object,
 * up to a max of the first 10 bytes if more than 10
 *
 * @p: Pointer to the Python Bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t	   i, size;
	PyBytesObject *p_copy;
	char		  *str;

	printf("[.] bytes object info\n");

	/* Check if object is a proper Bytes object */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* cast object it into a PyBytes Object */
	p_copy = (PyBytesObject *) p;
	str	   = p_copy->ob_sval;

	/* Get the size of the Python Byte object */
	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);

	/* Print the bytes as a string */
	printf("  trying string: %s\n", str);

	/* Print the first few bytes (max of 10) */
	size = size + 1;
	if (size > 10) /* adjust size to max of 10 */
		size = 10;
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", str[i]);
		if (i < size - 1) /* space between bytes except last one */
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Prints information about a Python list.
 * @p: Pointer to the Python list object.
 *
 * Description: This function retrieves and prints information about a
 * Python list, including its size, allocated memory, and element types.
 * It uses the Python C API to access the list and its elements.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t	i;
	Py_ssize_t	size;
	Py_ssize_t	allocated;
	PyObject   *element;
	const char *element_type;

	printf("[*] Python list info\n");
	/* Get the size of the Python list */
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	/* Get the allocated memory for the Python list */
	allocated = ((PyListObject *) p)->allocated;
	printf("[*] Allocated = %ld\n", allocated);

	/* Iterate over each element in the Python list */
	for (i = 0; i < size; i++)
	{
		/* Get the current element */
		element = PySequence_GetItem(p, i);

		/* Get the type name of the element */
		element_type = element->ob_type->tp_name;

		/* Print the index and type name of the element */
		printf("Element %ld: %s\n", i, element_type);

		if (PyBytes_Check(element))
			print_python_bytes(element);

		/* Manage memory */
		Py_DECREF(element);
	}
}
