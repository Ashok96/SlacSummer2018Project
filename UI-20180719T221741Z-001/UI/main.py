#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, uic
import sys
import time

form_class, base_class = uic.loadUiType('MoxaSetup.ui')

class MoxaSetupThread(QtCore.QThread):
    """MoxaSetup Thread"""
    def __init__(self, lock, parent = None):
        super(MoxaSetupThread, self).__init__(parent)
        self.lock      = lock
        self.mutex     = QtCore.QMutex()
        self.stopped   = False
        self.completed = False
        self.assign = False

    def initialize(self, current_action):
        self.current_action = current_action
        self.stopped        = False
        self.completed      = False
        return True

    def run(self):
        if self.current_action == 'setup':
            self._setup()
        if self.current_action == 'backup':
            self._backup()
        if self.current_action == 'restore':
            self._restore()
        if self.current_action == 'exit':
            self._shutdown()
        
    def _setup(self):
        """TBD - Setup MOXA with DHCP and users priviledges"""
        print('From Thread: Calling Setup method')
        time.sleep(4) # just a dummy to demonstrate the thread...
        self.emit(QtCore.SIGNAL("setpBsetup"), True)

    def _backup(self):
        """TBD - Backup current configuraton to file"""
        print('From Thread: Backup configuration...')
        self.emit(QtCore.SIGNAL("setpBbackup"), True)

    def _restore(self):
        """TBD - Restore configuration from file"""
        print('From Thread: Restore configuration...')
        self.emit(QtCore.SIGNAL("setpBrestore"), True)

    def _shutdown(self):
        """TBD - Shutting down the system"""
        print('From Thread: Shutting down the system...')
        self.emit(QtCore.SIGNAL("setpBexit"), True)

    def stop(self):
        try:
            self.mutex.lock()
            self.stopped = True
        finally:
            self.mutex.unlock()

    def isStopped(self):
        try:
            self.mutex.lock()
            return self.stopped
        finally:
            self.mutex.unlock()

#    def outprint(self, msg):
#        self.emit(QtCore.SIGNAL("pmsg(QString)"), msg)

#    def outdialog(self, mode, inp1, inp2, inp3):
#        sig3 = QtCore.SIGNAL("dialog(QString, QString, QString, QString)")
#        self.emit(sig3 , mode, inp1, inp2, inp3)

class MoxaSetupForm(QtGui.QWidget, form_class):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        super(MoxaSetupForm, self).__init__(parent)

        self.setupUi(self)

        self.lock = QtCore.QReadWriteLock()
        self.MoxaSetupThread = MoxaSetupThread(self.lock, self)

        self._initActions()           # setup button actions

    def _initActions(self):
        obj = QtCore.QObject
        sig1 = QtCore.SIGNAL("clicked()")
        sig2 = QtCore.SIGNAL("setpBsetup")
        sig3 = QtCore.SIGNAL("setpBbackup")
        sig4 = QtCore.SIGNAL("setpBrestore")
        sig5 = QtCore.SIGNAL("setpBexit")

        obj.connect(self.pB_SETUP       , sig1, self._setup)
        obj.connect(self.pB_EXIT        , sig1, self._exit)
        obj.connect(self.pB_BACKUP      , sig1, self._backup)
        obj.connect(self.pB_RESTORE     , sig1, self._restore)

        obj.connect(self.MoxaSetupThread, sig2, self._pBsetup)
        obj.connect(self.MoxaSetupThread, sig3, self._pBbackup)
        obj.connect(self.MoxaSetupThread, sig4, self._pBrestore)
        obj.connect(self.MoxaSetupThread, sig5, self._pBexit)

        #self.pB_BACKUP.setDisabled(True)
        #self.pB_RESTORE.setDisabled(True)

    def _setup(self):
        '''TBD - Sets MOXA to DHCP and setup all user and permission levels'''
        '''      Starts the thread MoxaSetupThread process                 '''

        # Check for thread instance:
        if self.MoxaSetupThread.isRunning():
            self.MoxaSetupThread.terminate()
            self.MoxaSetupThread.wait()
            self.MoxaSetupThread.stop()
            return False

        # Call Moxa Setup Thread:
        self.MoxaSetupThread.wait()

        # HERE THE LIST OF PARAMETERS NEEDED BY THE THREAD
        self.MoxaSetupThread.initialize('setup')

        # Disable setup button:
        self.pB_SETUP.setDisabled(True)
        self._startThread()
        return True

    def _pBsetup(self, action):
        if action == True:
            self.pB_SETUP.setDisabled(False)
        elif action == False:
            self.pB_SETUP.setDisabled(True)

    def _exit(self):
        '''TBD - Shutdown the system'''
        self.MoxaSetupThread.initialize('exit')
        self._startThread()

    def _pBexit(self, action):
        if action == True:
            self.pB_EXIT.setDisabled(False)
        elif action == False:
            self.pB_EXIT.setDisabled(True)

    def _backup(self):
        '''TBD - Saves the current configuration'''
        self.MoxaSetupThread.initialize('backup')
        self._startThread()
   
    def _pBbackup(self, action):
        if action == True:
            self.pB_BACKUP.setDisabled(False)
        elif action == False:
            self.pB_BACKUP.setDisabled(True)

    def _restore(self):
        '''TBD - Loads the saved configuration'''
        self.MoxaSetupThread.initialize('restore')
        self._startThread()

    def _pBrestore(self, action):
        if action == True:
            self.pB_RESTORE.setDisabled(False)
        elif action == False:
            self.pB_RESTORE.setDisabled(True)

    def _startThread(self):
        self.MoxaSetupThread.start()



if __name__ == "__main__":
    # ---------------------------------------------------------------------------
    style = {'CL' : 'Cleanlooks', 'XP': 'WindowsXP', 'PL' : 'Plastique'}
    app   = QtGui.QApplication(sys.argv)
    app.setStyle(style['PL'])
    app.setPalette(app.style().standardPalette())
    # ---------------------------------------------------------------------------

    try:
        MoxaSetup = MoxaSetupForm()
        if MoxaSetup:
            MoxaSetup.show()

        sys.exit(app.exec_())
    except (KeyboardInterrupt, SystemExit):
        pass
