import random
import numpy as np

def normal_dice(miu,sigma,nums = 1)->list:
    if nums > 500 or nums < 0:
        raise Exception("掷骰子数错误，不要超过500也不要小于0")
    return np.random.normal(miu,sigma,nums).tolist()

def poi_dice(lam,nums = 1)->list:
    if nums > 500 or nums < 0:
        raise Exception("掷骰子数错误，不要超过500也不要小于0")
    return np.random.poisson(lam,nums).tolist()

def uni_dice(start,end,nums = 1)->list:
    if nums > 500 or nums < 0:
        raise Exception("掷骰子数错误，不要超过500也不要小于0")
    return np.random.randint(start,end,nums).tolist()

def generate_final_information(ans_list,is_statistic):
    ans = ""
    cnt = 0
    if len(ans_list) <= 50:
        ans += f"下面是掷骰子结果:\n"
        for f in ans_list:
            ans += f"{f:.5f}\n"
    else:
        ans += f"您掷了{len(ans_list)}个骰子，数量过大，因此只会为您展示统计结果\n"

    ans += f"下面是掷骰子的统计结果结果:\n"
    if (is_statistic):
        ans += f"均值:{np.mean(ans_list):.5f}\n"
        ans += f"方差:{np.var(ans_list):.5f}\n"
    return ans

def interface_roll_dice_introduction(args):
    str_fast = "快速生成骰子: 语法:/掷骰子 最大值\n例如/掷骰子 10，则生成一个1到10之间的随机数\n"
    str_normal_fast = "快速生成均匀分布骰子: 语法:/掷骰子 最小值 最大值\n例如/掷骰子 1 6，则生成一个1到6之间的随机数\n"
    str_poi = "泊松分布: 语法:/掷骰子 poi λ (投掷数量)\n例如/掷骰子 poi 1 10，则按照泊松分布生成10个均值为1的随机数\n"
    str_uni = "均匀分布: 语法:/掷骰子 uni 最小值 最大值 (投掷数量)\n例如/掷骰子 uni 1 6，则按照均匀分布生成1个1到6之间的随机数\n"
    str_norm = "正态分布: 语法:/掷骰子 norm 均值 方差 (投掷数量)\n例如/掷骰子 norm 1 6 1000 statis，则按照正态分布生成1000个均值为1，方差为6的随机数，并且会统计出均值和方差\n"
    return "本功能支持投掷均匀分布、正态分布、泊松分布的骰子，要求输入的参数符合下面规范，且参数个数符合要求，并且掷骰子数大于0小于等于500，最后一个参数为statis可以进行统计\n" + str_fast + str_normal_fast + str_poi + str_uni + str_norm

def interface_roll_dice(args):
    # 用于掷骰子，本函数只用于处理掷骰子的数字选择
    start = 1
    end = 6
    ans_list = []
    is_statistic = False
    try:
        if(args[-1] == "statis"):
            is_statistic = True
            args = args[:-1]
        if(len(args) == 2):
            start = int(args[0])
            end = int(args[1])
            ans_list = uni_dice(start,end)
        elif(len(args) == 1):
            end = int(args[0])
            ans_list = uni_dice(start,end)
        elif(len(args) == 0):
            ans_list = uni_dice(start,end)
        else:
            if(args[0] == "poi"):
                lam = float(args[1])
                nums = 1
                if(len(args) >= 3):
                    nums = int(args[2])
                ans_list = poi_dice(lam,nums)
            elif(args[0] == "norm"):
                miu = float(args[1])
                sigma = float(args[2])
                nums = 1
                if(len(args) >= 4):
                    nums = int(args[3])
                ans_list = normal_dice(miu, np.sqrt(sigma), nums)
            elif(args[0] == "uni"):
                start = int(args[1])
                end = int(args[2])
                nums = 1
                if(len(args) >= 4):
                    nums = int(args[3])
                ans_list = uni_dice(start,end,nums)
            else:
                raise Exception("错误的掷骰子!")
    except:
        return f"错误的掷骰子!\n{interface_roll_dice_introduction(args)}"
    return f"掷骰子的结果是:{generate_final_information(ans_list,is_statistic)}"

if __name__ == '__main__':
    print(interface_roll_dice(["uni","0","10","100","statis"]))
