import javax.swing.*;

public class BankAccount {
    private int balance;
    private Person owner;

    public void setBalance(int newBalance) {
        if (newBalance >= 0) {
            balance = newBalance;
        }
    }

    public int getBalance() {
        return balance;
    }

    public void setOwner(Person newOwner) {
        owner = newOwner;
    }

    public Person getOwner() {
        return owner;
    }

    // 파라미터 : 입금할 액수(int)
    // 리턴값 : 성공 여부(boolean)

    boolean deposit(int amount) {
        if (amount < 0 || owner.getCashAmount() < amount) {
            System.out.println("입금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            System.out.println("false");
            return false;
        } else {
            balance += amount;
            owner.setCashAmount(owner.getCashAmount() - amount);
            System.out.println(amount + "원 입금하였습니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            System.out.println("true");
            return true;
        }
    }

    public boolean deposit(double amount, double exchangeRate) {
        System.out.println("");
        return deposit((int) (amount * exchangeRate));
    }

    // 파라미터 : 출금 액수(int)
    // 리턴값 : 성공 여부(boolean)
    boolean withdraw(int amount) {
        if (amount < 0 || amount > balance) {
            System.out.println("출금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            System.out.println("false");
            return false;
        } else {
            balance -= amount;
            getOwner().setCashAmount(getOwner().getCashAmount() + amount);
            System.out.println(amount + "원 출금하였습니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            System.out.println("true");
            return true;
        }
    }

    public boolean transfer(Person to, int amount) {
        if (amount >= 0 || amount > balance) {
            balance -= amount;
            to.getAccount().setBalance(to.getAccount().getBalance() + amount);
            System.out.println("true - from: [" + owner.getName() + "], to: [" + to.getName() + "], amount: ["
                    + amount + "], balance: [" + to.getAccount().getBalance() + "]");
            return true;
        } else {
            System.out.println("false - from: [" + owner.getName() + "], to: [" + to.getName() + "], amount: ["
                    + amount + "], balance: [" + to.getAccount().getBalance() + "]");
            return false;
        }
    }

    public boolean transfer(BankAccount to, int amount) {
        if (amount >= 0 || amount > balance) {
            balance -= amount;
            to.balance += amount;
            System.out.println("true - from: [" + owner.getName() + "], to: [" + to.getOwner().getName() + "], amount: ["
                    + amount + "], balance: [" + balance + "]");
            return true;
        } else {
            System.out.println("false - from: [" + owner.getName() + "], to: [" + to.getOwner().getName() + "], amount: ["
                    + amount + "], balance: [" + balance + "]");
            return false;
        }

        // 파라미터_1 : 받는 사람(Person)
        // 파라미터_2 : 이체할 금액(int)
        // 리턴값 : 성공 여부(boolean)

//    boolean transfer(Person to, int amount) {
//
//    }
    }
}