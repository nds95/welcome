public class BankAccount {
    int balance;
    Person owner;

    // 파라미터 : 입금할 액수(int)
    // 리턴값 : 성공 여부(boolean)

    boolean deposit(int amount) {
        if (amount < 0 || owner.cashAmount < amount) {
            System.out.println("입금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.cashAmount);
            return false;
        } else {
            balance += amount;
            owner.cashAmount -= amount;
            System.out.println(amount + "원 입금하였습니다. 잔고: " + balance + "원, 현금: " + owner.cashAmount);
            return true;
        }
    }

    // 파라미터 : 출금 액수(int)
    // 리턴값 : 성공 여부(boolean)
    boolean withdraw(int amount) {
        if (amount < 0 || amount > balance) {
            System.out.println("출금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.cashAmount);
            return false;
        } else {
            balance -= amount;
            owner.cashAmount += amount;
            System.out.println(amount + "원 출금하였습니다. 잔고: " + balance + "원, 현금: " + owner.cashAmount);
            return true;
        }
    }

    // 파라미터_1 : 받는 사람(Person)
    // 파라미터_2 : 이체할 금액(int)
    // 리턴값 : 성공 여부(boolean)

//    boolean transfer(Person to, int amount) {
//
//    }
}
