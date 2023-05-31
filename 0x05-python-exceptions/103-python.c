#include "Python.h"
#include <math.h>
#include <stdio.h>

/**
 * has_precision_one - Checks if a double has a precision of one
 * @number: Pointer to the Python Bytes object.
 *
 * Return: 1 if precision is 1 and 0 if otherwise
 */
int has_precision_one(double number)
{
	double rounded	  = round(number);
	double difference = fabs(number - rounded);

	return (difference == 0);
}

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
 * print_python_float - Prints information about a Python float object.
 * @p: Pointer to the Python float object.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_object;
	double		   float_value;

	printf("[.] float object info\n");

	/* check if object is a proper float object */
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	/* cast object into float object */
	float_object = (PyFloatObject *) p;
	/* grab float value */
	float_value = float_object->ob_fval;
	/* print float value */
	if (has_precision_one(float_value))
		printf("  value: %.1f\n", float_value);
	else /* variable precision */
		printf("  value: %.16g\n", float_value);
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
	Py_ssize_t	  i, size, allocated;
	PyObject	 *element;
	const char	 *element_type;
	PyListObject *list;

	printf("[*] Python list info\n");
	/* Check if object is a proper List object */
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	/* cast object into list object */
	list = (PyListObject *) p;

	/* Get the size of the Python list */
	size = ((PyVarObject *) (p))->ob_size;
	printf("[*] Size of the Python List = %ld\n", size);

	/* Get the allocated memory for the Python list */
	allocated = ((PyListObject *) p)->allocated;
	printf("[*] Allocated = %ld\n", allocated);

	/* Iterate over each element in the Python list */
	for (i = 0; i < size; i++)
	{
		/* Get the current element */
		element = list->ob_item[i];
		/* Get the type name of the element */
		element_type = element->ob_type->tp_name;
		/* Print the index and type name of the element */
		printf("Element %ld: %s\n", i, element_type);
		if (PyBytes_Check(element)) /* check if el is byte object */
			print_python_bytes(element);
		if (PyFloat_Check(element)) /* check if el is float object */
			print_python_float(element);
	}
}
