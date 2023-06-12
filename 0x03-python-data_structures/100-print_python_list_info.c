#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: pointer to object of type PyObject
 *
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *listObj = (PyListObject *)p;
	Py_ssize_t size = Py_SIZE(listObj);
	Py_ssize_t i, allocated = listObj->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = item->ob_type->tp_name;

		printf("Element %zd: %s\n", i, typeName);
	}
}
