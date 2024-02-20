public class Animal {
    // Thuộc tính (fields)
    private String name;
    private int age;

    // Constructor
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Phương thức
    public void eat() {
        System.out.println(name + " đang ăn.");
    }

    public void sleep() {
        System.out.println(name + " đang ngủ.");
    }

    public void makeSound() {
        System.out.println(name + " đang kêu.");
    }

    // Phương thức getter và setter
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    // Phương thức main để kiểm tra lớp Animal
    public static void main(String[] args) {
        Animal cat = new Animal("Meo", 2);
        cat.eat();
        cat.sleep();
        cat.makeSound();

        Animal dog = new Animal("Gau", 3);
        dog.eat();
        dog.sleep();
        dog.makeSound();
    }
}
