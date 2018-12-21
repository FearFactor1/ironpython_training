import clr
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublickKeyToken=31bf3856ad')
from System.Windows.Automation import *

import time

def test_something():
    application = Application.Launch("C:\\Program Files (x86)\\GAS Softwares\\Free Address Book\\AddressBook.exe")
    main_window = application.GetWindow("Free Address Book")
    main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
    modal = main_window.ModalWindow("Group editor")

    modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
    modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter('test group')
    Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)

    time.sleep(10)

    modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()

    main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()
