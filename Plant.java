package cs3337;

public class Plant {
	static int count = 0;
	int id;
	String name;
	double temp = 0.0;

	public Plant(String nameIn, double tempIn) {
		this.name = nameIn; this.temp = tempIn; this.id = count++;
	}
	
	public int getId() { return this.id; }
	
	public void setName(String nameIn) { this.name = nameIn; }
	public String getName() { return this.name; }
	
	public void setTemp(double tempIn) { this.temp = tempIn; }
	public double getTemp() { return this.temp; }
}