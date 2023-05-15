#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @p: Pointer to the Python list object.
 *
 * Description: This function retrieves and prints information about a
 * Python list, including its size, allocated memory, and element types.
 * It uses the Python C API to access the list and its elements.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t	i;
	Py_ssize_t	size;
	Py_ssize_t	allocated;
	PyObject   *element;
	const char *element_type;

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
		element = PyList_GetItem(p, i);

		/* Get the type name of the element */
		element_type = element->ob_type->tp_name;

		/* Print the index and type name of the element */
		printf("Element %ld: %s\n", i, element_type);
	}
}
