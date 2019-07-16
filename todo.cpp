#include<iostream>
#include<string>

class Todolist {
private:
	int number;
	std::string todo;
	std::string dateby;
	bool finished;

public:
	void read_data();


	//void add_title(std::string new_title);
	//std::string get_title();

	//void add_artist(std::string new_artist);
	//std::string get_artist();

};

// add Song method definitions here:
void Todolist::read_data() {
	std::cout << "Task number: ";
	std::cin >> number;
	std::cout << "\nWhat needs to be done? ";
	std::cin >> todo;
	std::cout << "When does it need to be done by? ";
	std::cin >> dateby;
	std::cout << "Is it done? ";
	std::cin >> finished;
	//title = new_title;
}


void Todolist::show_data() {
	std::cout << "Task number: " << number << endl;
	std::cout << "To do: " << todo << endl;
	std::cout << "Deadline: " << dateby << endl;
	std::cout<< "Progre"

}

void Todolist::edit_data() {


}


void Todolist::





std::string Song::get_title() {

  return title;

}

void Song::add_artist(std::string new_artist) {

  artist = new_artist;

}

std::string Song::get_artist() {

  return artist;

}

int main() {

	Song electric_relaxation;

	electric_relaxation.add_artist("A Tribe Called Quest");
	std::cout << electric_relaxation.get_artist();

}


