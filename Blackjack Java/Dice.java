public class Dice {
  public static void main(String args[]){
  }

  public int roll(){
    int card = (int)((Math.random() * 6)+1);
    return card;
  }
}