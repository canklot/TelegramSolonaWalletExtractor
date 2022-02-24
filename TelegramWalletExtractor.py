import json

def DuplicateRemover(mylist):
    mylist = list(dict.fromkeys(mylist))
    return mylist

def GetFile(FilePath):
    with open(FilePath, "r",encoding="utf8") as file:
        Data = json.load(file)
        return Data
    
def FindWalletAddress(Data):
    WalletList = []
    for Message in Data["messages"]:
        text = Message["text"]
        if (len(text)==44):
            WalletList.append(text)
    WalletCount = len(WalletList)
    WalletList = DuplicateRemover(WalletList)
    WalletCountIndividual = len(WalletList)
    return WalletList

def WriteToFile(Data):
    with open("TelegramResults.txt",'w',encoding = 'utf-8') as f:
        for line in Data:
            f.write(line+"\n")
def main():
    print ("Working")
    Data = GetFile("../telegram.json")
    WalletList = FindWalletAddress(Data)
    WriteToFile(WalletList)
    print ("Thank you")
    
if __name__ == "__main__":
    main()
