#include<iostream>
#include<string>
#include<stdio.h>



class Todolist {
private:
	int number;
	std::string todo;
	std::string dateby;
	bool finished;

public:
	void read_data();
	void show_data();
	void input_entry();
	void show_entry();
	void check_entry();
	void delete_entry();



};

void Todolist::read_data() {
	std::cout << "Task number: ";
	std::cin >> number;
	std::cout << "\nWhat needs to be done? ";
	std::cin >> todo;
	std::cout << "\nWhen does it need to be done by? ";
	std::cin >> dateby;
	std::cout << "\nIs it done? ";
	std::cin >> finished;
	std::cout << std::endl;
}


void Todolist::show_data() {
	std::cout << "Task number: " << number << std::endl;
	std::cout << "To do: " << todo << std::endl;
	std::cout << "Deadline: " << dateby << std::endl;
	std::cout << "Progress: " << finished << std::endl;
	std::cout << "___________________________" << std::endl;
}

void Todolist::input_entry() {
	read_data();
}

void Todolist::show_entry() {
	show_data();
}

void Todolist::check_entry() {
	bool done;
	std::cout << "\n There progress of object " << finished;
	std::cout << "\n Enter the new progress: ";
	std::cin >> finished;
	show_entry();

}

void Todolist::delete_entry() {
	int n;
	std::cout << "\n Enter task to Delete: ";
	std::cin >> n;


}


int main() {
	Todolist clas;
	int number;
	while (true) {
		std::cout << "\n\t1-->Add a thing that needs to be done";
		std::cout << "\n\t2-->Show what needs to be done ";
		std::cout << "\n\t3-->Check something off ";
		std::cout << "\n\t4-->Delete a entry";
		std::cout << "\nEnter your choice: ";
		std::cin >> number;

		switch (number) {
		case 1:
			clas.input_entry();
			break;
		
		case 2:
			clas.show_entry();
			break;

		case 3:
			clas.check_entry();
			break;

		case 4:
			clas.delete_entry();
			break;

		default:
			std::cout << "\nEnter corret choice";
			exit(0);
		}
	}

	system("pause");
	return 0;
}
