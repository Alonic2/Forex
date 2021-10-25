import yfinance as yf
import fire

def Stock(name,Start,End):

    Data = yf.download(str(name), start=str(Start), end=str(End))
    Data.to_csv(f"{name}.csv")

if __name__ == '__main__':
    fire.Fire()