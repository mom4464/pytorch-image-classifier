
from utils import check_data_and_lable
import torch
from dataloader import trainloader
from train import start_training
from model import net,optimizer,criterion
from validation import  random_check , overall_check ,each_class_check
from convert import start_converting

PATH = '/App/data/cifar_net.pth'


if __name__ == '__main__':
 #check_data_and_lable()

 # stat_dic=start_training(net,5,trainloader,optimizer,criterion)
 # print('saving checkpoint to ',PATH)
 # torch.save(stat_dic, PATH)

 #random_check(net,PATH)
 # overall_check(net,PATH)
 # each_class_check(net,PATH)
 x = torch.ones((4, 3, 32, 32)).cuda()
 #dataiter = iter(trainloader)
 # print(dataiter.next())
 #x=dataiter.next()
 start_converting(net,x)
