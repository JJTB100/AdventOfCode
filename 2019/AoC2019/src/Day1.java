public class Day1 {
    public static void main(String[] args) throws Exception {
        String data = FileUtil.Read("Day1.txt");
        int total = 0;
        for (String line : data.split("\n")) {
            total += getFuel(Integer.parseInt(line.trim()));
        }
        System.out.println(total);
    }

    private static int getFuel(int mass) {
        int total = (mass / 3) - 2;
        // Base
        if (total <= 0) {
            return 0;
        }
        return total + getFuel(total);
    }
}
