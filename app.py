#!flask/bin/python
from flask import Flask,jsonify
from flask_cors import CORS
from datetime import datetime
import random
import requests

app = Flask(__name__)
CORS(app)

datetimeNow = datetime.now()

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

orchestration_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Orchestration',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456789,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Orchestration',
    'projectName' : 'Orchestration',
    'projectId' : 'Orchestration',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Orchestration',
  'buildTypeInternalId' : 'Orchestration',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 685 out of 754 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

orchestration_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Orchestration',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Orchestration',
    'projectName' : 'Orchestration',
    'projectId' : 'Orchestration',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Orchestration',
  'buildTypeInternalId' : 'Orchestration',
  'branchName' : 'develop',
  'statusText' : 'Successful. 754 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

orchestration_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Orchestration',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Orchestration',
    'projectName' : 'Orchestration',
    'projectId' : 'Orchestration',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Orchestration',
  'buildTypeInternalId' : 'Orchestration',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

registration_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Registration',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Petr',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456789,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Registration',
    'projectName' : 'Registration',
    'projectId' : 'Registration',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Registration',
  'buildTypeInternalId' : 'Registration',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 450 out of 500 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

registration_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Registration',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Petr',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Petr'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Registration',
    'projectName' : 'Registration',
    'projectId' : 'Registration',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Registration',
  'buildTypeInternalId' : 'Registration',
  'branchName' : 'develop',
  'statusText' : 'Successful. 500 Tests completed',
  'cusJerry-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

registration_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Registration',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Petr',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Petr'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Registration',
    'projectName' : 'Registration',
    'projectId' : 'Registration',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Registration',
  'buildTypeInternalId' : 'Registration',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'cusJerry-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

ingestion_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Ingestion',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Davos',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Davos'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456749,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Ingestion',
    'projectName' : 'Ingestion',
    'projectId' : 'Ingestion',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Ingestion',
  'buildTypeInternalId' : 'Ingestion',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 199 out of 200 completed',
  'cusPluto-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

ingestion_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Ingestion',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Davos',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Davos'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Ingestion',
    'projectName' : 'Ingestion',
    'projectId' : 'Ingestion',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Ingestion',
  'buildTypeInternalId' : 'Ingestion',
  'branchName' : 'develop',
  'statusText' : 'Successful. 754 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

ingestion_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Ingestion',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Davos',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Davos'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Ingestion',
    'projectName' : 'Ingestion',
    'projectId' : 'Ingestion',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Ingestion',
  'buildTypeInternalId' : 'Ingestion',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'cusPluto-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

discovery_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Discovery',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Sansa',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Sansa'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456709,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Discovery',
    'projectName' : 'Discovery',
    'projectId' : 'Discovery',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Discovery',
  'buildTypeInternalId' : 'Discovery',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 111 out of 142 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

discovery_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Discovery',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Sansa',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Sansa'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Discovery',
    'projectName' : 'Discovery',
    'projectId' : 'Discovery',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Discovery',
  'buildTypeInternalId' : 'Discovery',
  'branchName' : 'develop',
  'statusText' : 'Successful. 142 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

discovery_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Discovery',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Sansa',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Sansa'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Discovery',
    'projectName' : 'Discovery',
    'projectId' : 'Discovery',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Discovery',
  'buildTypeInternalId' : 'Discovery',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

security_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Security',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Danaerys',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Danaerys'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456789,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Security',
    'projectName' : 'Security',
    'projectId' : 'Security',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Security',
  'buildTypeInternalId' : 'Security',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 345 out of 900 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

security_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Security',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Danaerys',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Danaerys'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Security',
    'projectName' : 'Security',
    'projectId' : 'Security',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Security',
  'buildTypeInternalId' : 'Security',
  'branchName' : 'develop',
  'statusText' : 'Successful. 900 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

security_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Security',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Danaerys',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Danaerys'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Security',
    'projectName' : 'Security',
    'projectId' : 'Security',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Security',
  'buildTypeInternalId' : 'Security',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

portal_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Portal',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Drogo',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Drogo'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456789,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Portal',
    'projectName' : 'Portal',
    'projectId' : 'Portal',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Portal',
  'buildTypeInternalId' : 'Portal',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 685 out of 698 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

portal_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Portal',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Drogo',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Drogo'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Portal',
    'projectName' : 'Portal',
    'projectId' : 'Portal',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Portal',
  'buildTypeInternalId' : 'Portal',
  'branchName' : 'develop',
  'statusText' : 'Successful. 698 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

portal_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Portal',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Drogo',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Drogo'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Portal',
    'projectName' : 'Portal',
    'projectId' : 'Portal',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Portal',
  'buildTypeInternalId' : 'Portal',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

services_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Services',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Cercei',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Cercei'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456789,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Services',
    'projectName' : 'Services',
    'projectId' : 'Services',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Services',
  'buildTypeInternalId' : 'Services',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 123 out of 800 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

services_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Services',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Cercei',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Cercei'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Services',
    'projectName' : 'Services',
    'projectId' : 'Services',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Services',
  'buildTypeInternalId' : 'Services',
  'branchName' : 'develop',
  'statusText' : 'Successful. 800 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

services_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Services',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Cercei',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Cercei'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Services',
    'projectName' : 'Services',
    'projectId' : 'Services',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Services',
  'buildTypeInternalId' : 'Services',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

commons_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Commons',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jamie',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jamie'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456789,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Commons',
    'projectName' : 'Commons',
    'projectId' : 'Commons',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Commons',
  'buildTypeInternalId' : 'Commons',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 685 out of 744 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

commons_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Commons',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jamie',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jamie'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Commons',
    'projectName' : 'Commons',
    'projectId' : 'Commons',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Commons',
  'buildTypeInternalId' : 'Commons',
  'branchName' : 'develop',
  'statusText' : 'Successful. 744 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

commons_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Commons',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jamie',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jamie'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Commons',
    'projectName' : 'Commons',
    'projectId' : 'Commons',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Commons',
  'buildTypeInternalId' : 'Commons',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

core_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Core',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Varys',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Varys'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456789,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Core',
    'projectName' : 'Core',
    'projectId' : 'Core',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Core',
  'buildTypeInternalId' : 'Core',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 685 out of 754 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

core_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Core',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Varys',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Varys'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Core',
    'projectName' : 'Core',
    'projectId' : 'Core',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Core',
  'buildTypeInternalId' : 'Core',
  'branchName' : 'develop',
  'statusText' : 'Successful. 754 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

core_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Core',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Varys',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Varys'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Core',
    'projectName' : 'Core',
    'projectId' : 'Core',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Core',
  'buildTypeInternalId' : 'Core',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

utilities_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Utilities',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Arya',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Arya'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456689,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Utilities',
    'projectName' : 'Utilities',
    'projectId' : 'Utilities',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Utilities',
  'buildTypeInternalId' : 'Utilities',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 500 out of 1000 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

utilities_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Utilities',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Arya',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Arya'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Utilities',
    'projectName' : 'Utilities',
    'projectId' : 'Utilities',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Utilities',
  'buildTypeInternalId' : 'Utilities',
  'branchName' : 'develop',
  'statusText' : 'Successful. 1000 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

utilities_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Utilities',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Arya',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Arya'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Utilities',
    'projectName' : 'Utilities',
    'projectId' : 'Utilities',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Utilities',
  'buildTypeInternalId' : 'Utilities',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

maintenance_running_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Maintenance',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Tyrion',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Tyrion'
    } ],
    'count' : 123,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456889,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456999
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Maintenance',
    'projectName' : 'Maintenance',
    'projectId' : 'Maintenance',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'RUNNING',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'running' : 'true',
  'buildTypeId' : 'Maintenance',
  'buildTypeInternalId' : 'Maintenance',
  'branchName' : 'develop',
  'statusText' : 'In progress. Tests 85 out of 200 completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

maintenance_finished_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Maintenance',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Tyrion',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Tyrion'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Maintenance',
    'projectName' : 'Maintenance',
    'projectId' : 'Maintenance',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Maintenance',
  'buildTypeInternalId' : 'Maintenance',
  'branchName' : 'develop',
  'statusText' : 'Successful. 200 Tests completed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

maintenance_pending_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Maintenance',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Tyrion',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Tyrion'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Maintenance',
    'projectName' : 'Maintenance',
    'projectId' : 'Maintenance',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'FAILURE',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Maintenance',
  'buildTypeInternalId' : 'Maintenance',
  'branchName' : 'develop',
  'statusText' : 'OrchestratingBean LoginTest Failed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

coverage_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Coverage',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Tyrion',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Tyrion'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Coverage',
    'projectName' : 'Coverage',
    'projectId' : 'Coverage',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Coverage',
  'buildTypeInternalId' : 'Coverage',
  'branchName' : 'develop',
  'statusText' : '83%',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

bugs_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Bugs',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Hodor',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Hodor'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Bugs',
    'projectName' : 'Bugs',
    'projectId' : 'Bugs',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Bugs',
  'buildTypeInternalId' : 'Bugs',
  'branchName' : 'develop',
  'statusText' : '12',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

vulnerabilities_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Vulnerabilities',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Tormund',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Tormund'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Vulnerabilities',
    'projectName' : 'Vulnerabilities',
    'projectId' : 'Vulnerabilities',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Vulnerabilities',
  'buildTypeInternalId' : 'Vulnerabilities',
  'branchName' : 'develop',
  'statusText' : '22',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

codeSmells_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'CodeSmells',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Bran',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Bran'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'CodeSmells',
    'projectName' : 'CodeSmells',
    'projectId' : 'CodeSmells',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'CodeSmells',
  'buildTypeInternalId' : 'CodeSmells',
  'branchName' : 'develop',
  'statusText' : '642',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

uds_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'UDS',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'UDS',
    'projectName' : 'UDS',
    'projectId' : 'UDS',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'UDS',
  'buildTypeInternalId' : 'UDS',
  'branchName' : 'develop',
  'statusText' : 'UP',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

uds_response_down = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'UDS',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'UDS',
    'projectName' : 'UDS',
    'projectId' : 'UDS',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'UDS',
  'buildTypeInternalId' : 'UDS',
  'branchName' : 'develop',
  'statusText' : 'DOWN',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

uds_response_starting = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'UDS',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'UDS',
    'projectName' : 'UDS',
    'projectId' : 'UDS',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'UDS',
  'buildTypeInternalId' : 'UDS',
  'branchName' : 'develop',
  'statusText' : 'STARTING',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

red = 'RED'

yellow = 'YELLOW'

green = 'GREEN'

fiftyfive = '55'
seventy = '70'
ninety = '90'
thirty = '30'

memory1_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Memory',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Memory',
    'projectName' : 'Memory',
    'projectId' : 'Memory',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Memory',
  'buildTypeInternalId' : 'Memory',
  'branchName' : 'develop',
  'statusText' : '50 % 2048MB used',
  'messageText': 'Memory Consumed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
memory2_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Memory',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Memory',
    'projectName' : 'Memory',
    'projectId' : 'Memory',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Memory',
  'buildTypeInternalId' : 'Memory',
  'branchName' : 'develop',
  'statusText' : '79 % 2048MB used',
  'messageText' : 'Memory Consumed',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
memory3_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Memory',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Memory',
    'projectName' : 'Memory',
    'projectId' : 'Memory',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Memory',
  'buildTypeInternalId' : 'Memory',
  'branchName' : 'develop',
  'statusText' : '98 % 2048MB used',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'messageText' : 'Memory Consumed',
  'finishDate' : datetimeNow
}

cpu1_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Cpu',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Cpu',
    'projectName' : 'Cpu',
    'projectId' : 'Cpu',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Cpu',
  'buildTypeInternalId' : 'Cpu',
  'branchName' : 'develop',
  'statusText' : '66%',
  'messageText': 'Cpu Usage',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
cpu2_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Cpu',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Cpu',
    'projectName' : 'Cpu',
    'projectId' : 'Cpu',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Cpu',
  'buildTypeInternalId' : 'Cpu',
  'branchName' : 'develop',
  'statusText' : '23%',
  'messageText': 'Cpu Usage',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
cpu3_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Cpu',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Cpu',
    'projectName' : 'Cpu',
    'projectId' : 'Cpu',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Cpu',
  'buildTypeInternalId' : 'Cpu',
  'branchName' : 'develop',
  'statusText' : '89%',
  'messageText': 'Cpu Usage',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

diskspace1_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Diskspace',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Diskspace',
    'projectName' : 'Diskspace',
    'projectId' : 'Diskspace',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Diskspace',
  'buildTypeInternalId' : 'Diskspace',
  'branchName' : 'develop',
  'statusText' : 'Used 41G      Free 410G',
  'messageText': 'Diskspace Stats',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
diskspace2_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Diskspace',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Diskspace',
    'projectName' : 'Diskspace',
    'projectId' : 'Diskspace',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Diskspace',
  'buildTypeInternalId' : 'Diskspace',
  'branchName' : 'develop',
  'statusText' : 'Used 159G      Free 410G',
  'messageText': 'Diskspace Stats',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
diskspace3_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Diskspace',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Diskspace',
    'projectName' : 'Diskspace',
    'projectId' : 'Diskspace',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Diskspace',
  'buildTypeInternalId' : 'Diskspace',
  'branchName' : 'develop',
  'statusText' : 'Used 350G      Free 410G',
  'messageText': 'Diskspace Stats',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

database1_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Database',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Database',
    'projectName' : 'Database',
    'projectId' : 'Database',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Database',
  'buildTypeInternalId' : 'Database',
  'branchName' : 'develop',
  'statusText' : 'Active (Running)',
  'messageText': 'Mongo Status',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
database2_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Database',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Database',
    'projectName' : 'Database',
    'projectId' : 'Database',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Database',
  'buildTypeInternalId' : 'Database',
  'branchName' : 'develop',
  'statusText' : 'Down',
  'messageText': 'Mongo Stauts',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
database3_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Database',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Database',
    'projectName' : 'Database',
    'projectId' : 'Database',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Database',
  'buildTypeInternalId' : 'Database',
  'branchName' : 'develop',
  'statusText' : 'Active (Indexing)',
  'messageText': 'Mongo Stauts',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

dataLoad1_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'DataLoad',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'DataLoad',
    'projectName' : 'DataLoad',
    'projectId' : 'DataLoad',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'DataLoad',
  'buildTypeInternalId' : 'DataLoad',
  'branchName' : 'develop',
  'statusText' : '1233 Records uploaded-UAT',
  'messageText': 'Nymeria Server Status',
  'timeToComplete' : '44 minutes',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
dataLoad2_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'DataLoad',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'DataLoad',
    'projectName' : 'DataLoad',
    'projectId' : 'DataLoad',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'DataLoad',
  'buildTypeInternalId' : 'DataLoad',
  'branchName' : 'develop',
  'statusText' : '8322 Records uploaded-UAT',
  'messageText': 'Ghost Server Status',
  'timeToComplete' : '6 hours 23 minutes',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
dataLoad3_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'DataLoad',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'DataLoad',
    'projectName' : 'DataLoad',
    'projectId' : 'DataLoad',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'DataLoad',
  'buildTypeInternalId' : 'DataLoad',
  'branchName' : 'develop',
  'statusText' : '3509 Records uploaded-UAT',
  'messageText': 'Summer Server Status',
  'timeToComplete' : '3 hours 12 minutes',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

consumption1_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Consumption',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Consumption',
    'projectName' : 'Consumption',
    'projectId' : 'Consumption',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Consumption',
  'buildTypeInternalId' : 'Consumption',
  'branchName' : 'develop',
  'statusText' : '1314 events consumed in 1 Hour',
  'messageText': 'Lannisport Server Status',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
consumption2_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Consumption',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Consumption',
    'projectName' : 'Consumption',
    'projectId' : 'Consumption',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Consumption',
  'buildTypeInternalId' : 'Consumption',
  'branchName' : 'develop',
  'statusText' : '4312 events consumed in 1 Hour',
  'messageText': 'Winterfell Server Status',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}
consumption3_response = {
  'metadata' : {
    'data' : [ {
      'id' : 'aeiou'
    } ],
    'count' : 123
},
  'triggered' : {
    'date' : 'aeiou',
    'rawValue' : 'aeiou',
    'buildType' : 'Consumption',
    'details' : 'aeiou',
    'type' : 'aeiou',
    'user' : 'aeiou',
  },
  'lastChanges' : {
    'change' : [ {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jorah',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jorah'
    } ],
    'count' : 0,
    'prevHref' : 'aeiou',
    'href' : 'aeiou',
    'nextHref' : 'aeiou'
  },
  'id' : 123456789,
  'defaultBranch' : 'true',
  'compatibleAgents' : 'aeiou',
  'tags' : {
    'count' : 123,
    'tag' : [ {
      'owner' : 'aeiou',
      'private' : 'true',
      'name' : 'aeiou'
    } ]
  },
  'canceledInfo' : 'aeiou',
  'running-info' : {
    'estimatedTotalSeconds' : 123456799,
    'outdated' : 'true',
    'percentageComplete' : 123,
    'probablyHanging' : 'true',
    'currentStageText' : 'aeiou',
    'elapsedSeconds' : 123456799
  },
  'versionedSettingsRevision' : 'aeiou',
  'percentageComplete' : 123,
  'webUrl' : 'aeiou',
  'buildType' : {
    'name' : 'Consumption',
    'projectName' : 'Consumption',
    'projectId' : 'Consumption',
    'parameters' : 'aeiou',
    'locator' : 'aeiou'
  },
  'locator' : 'aeiou',
  'startDate' : 'aeiou',
  'status' : 'SUCCESS',
  'pinned' : 'true',
  'changes' : 'aeiou',
  'buildTypeId' : 'Consumption',
  'buildTypeInternalId' : 'Consumption',
  'branchName' : 'develop',
  'statusText' : '2254 Events consumed in last one hour',
  'messageText': 'Braavos Consumption Status',
  'custom-artifact-dependencies' : 'aeiou',
  'comment' : 'aeiou',
  'finishDate' : datetimeNow
}

changes = {
'change' : [
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    }
]
}

changes8 = {
'change' : [
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    }
]
}

changes10 = {
'change' : [
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    }
]
}

changes12 = {
'change' : [
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    }
]
}

changes14 = {
'change' : [
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
]
}

changes16 = {
'change' : [
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
        'date': 'aeiou',
        'files': {
            'file': [{
                'changeTypeComment': 'aeiou',
                'file': 'aeiou',
                'relative-file': 'aeiou',
                'after-revision': 'aeiou',
                'changeType': 'aeiou',
                'directory': 'true',
                'before-revision': 'aeiou'
            }],
            'count': 0
        },
        'comment': 'Meow',
        'id': 123456789,
        'href': 'aeiou',
        'user': 'Jon',
        'locator': 'aeiou',
        'parentChanges': 'aeiou',
        'username': 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
{
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
{
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
    {
      'date' : 'aeiou',
      'files' : {
        'file' : [ {
          'changeTypeComment' : 'aeiou',
          'file' : 'aeiou',
          'relative-file' : 'aeiou',
          'after-revision' : 'aeiou',
          'changeType' : 'aeiou',
          'directory' : 'true',
          'before-revision' : 'aeiou'
        } ],
        'count' : 0
      },
      'comment' : 'Meow',
      'id' : 123456789,
      'href' : 'aeiou',
      'user' : 'Jon',
      'locator' : 'aeiou',
      'parentChanges' : 'aeiou',
      'username' : 'Jon'
    },
]
}

@app.route('/app/teamcity/builds/buildType:(id:Orchestration),running:any,branch:develop', methods=['GET'])
def get_orchestrator():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(orchestration_running_response)
    if number == 2:
        return jsonify(orchestration_pending_response)
    if number == 3:
        return jsonify(orchestration_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Orchestration),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_orchestrator_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(orchestration_running_response)
    if number == 2:
        return jsonify(orchestration_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Orchestration),sinceChange:undefined,branch:develop',methods=['GET'])
def get_orchestrator_pending_response():
    return jsonify(changes)

@app.route('/app/teamcity/builds/buildType:(id:Registration),running:any,branch:develop', methods=['GET'])
def get_registration():
    number = 3
    print number
    if number == 1:
        return jsonify(registration_running_response)
    if number == 2:
        return jsonify(registration_pending_response)
    if number == 3:
        return jsonify(registration_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Registration),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_registration_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(registration_running_response)
    if number == 2:
        return jsonify(registration_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Registration),sinceChange:undefined,branch:develop',methods=['GET'])
def get_registration_pending_response():
    return jsonify(changes)

@app.route('/app/teamcity/builds/buildType:(id:Ingestion),running:any,branch:develop', methods=['GET'])
def get_ingestion():
    number = 3
    print number
    if number == 1:
        return jsonify(ingestion_running_response)
    if number == 2:
        return jsonify(ingestion_pending_response)
    if number == 3:
        return jsonify(ingestion_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Ingestion),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_ingestion_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(ingestion_running_response)
    if number == 2:
        return jsonify(ingestion_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Ingestion),sinceChange:undefined,branch:develop',methods=['GET'])
def get_ingestion_pending_response():
    return jsonify(changes)

@app.route('/app/teamcity/builds/buildType:(id:Security),running:any,branch:develop', methods=['GET'])
def get_security():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(security_running_response)
    if number == 2:
        return jsonify(security_pending_response)
    if number == 3:
        return jsonify(security_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Security),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_security_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(security_running_response)
    if number == 2:
        return jsonify(security_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Security),sinceChange:undefined,branch:develop',methods=['GET'])
def get_security_pending_response():
    return jsonify(changes8)

@app.route('/app/teamcity/builds/buildType:(id:Discovery),running:any,branch:develop', methods=['GET'])
def get_discovery():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(discovery_running_response)
    if number == 2:
        return jsonify(discovery_pending_response)
    if number == 3:
        return jsonify(discovery_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Discovery),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_discovery_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(discovery_running_response)
    if number == 2:
        return jsonify(discovery_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Discovery),sinceChange:undefined,branch:develop',methods=['GET'])
def get_discovery_pending_response():
    return jsonify(changes10)

@app.route('/app/teamcity/builds/buildType:(id:Portal),running:any,branch:develop', methods=['GET'])
def get_portal():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(portal_running_response)
    if number == 2:
        return jsonify(portal_pending_response)
    if number == 3:
        return jsonify(portal_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Portal),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_portal_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(portal_running_response)
    if number == 2:
        return jsonify(portal_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Portal),sinceChange:undefined,branch:develop',methods=['GET'])
def get_portal_pending_response():
    return jsonify(changes12)

@app.route('/app/teamcity/builds/buildType:(id:Services),running:any,branch:develop', methods=['GET'])
def get_services():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(services_running_response)
    if number == 2:
        return jsonify(services_pending_response)
    if number == 3:
        return jsonify(services_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Services),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_services_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(services_running_response)
    if number == 2:
        return jsonify(services_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Services),sinceChange:undefined,branch:develop',methods=['GET'])
def get_services_pending_response():
    return jsonify(changes14)


@app.route('/app/teamcity/builds/buildType:(id:Commons),running:any,branch:develop', methods=['GET'])
def get_commons():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(commons_running_response)
    if number == 2:
        return jsonify(commons_pending_response)
    if number == 3:
        return jsonify(commons_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Commons),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_commons_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(commons_running_response)
    if number == 2:
        return jsonify(commons_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Commons),sinceChange:undefined,branch:develop',methods=['GET'])
def get_commons_pending_response():
    return jsonify(changes14)



@app.route('/app/teamcity/builds/buildType:(id:Core),running:any,branch:develop', methods=['GET'])
def get_core():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(core_running_response)
    if number == 2:
        return jsonify(core_pending_response)
    if number == 3:
        return jsonify(core_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Core),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_core_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(core_running_response)
    if number == 2:
        return jsonify(core_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Core),sinceChange:undefined,branch:develop',methods=['GET'])
def get_core_pending_response():
    return jsonify(changes14)


@app.route('/app/teamcity/builds/buildType:(id:Utilities),running:any,branch:develop', methods=['GET'])
def get_utilities():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(utilities_running_response)
    if number == 2:
        return jsonify(utilities_pending_response)
    if number == 3:
        return jsonify(utilities_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Utilities),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_uitlities_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(utilities_running_response)
    if number == 2:
        return jsonify(utilities_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Utilities),sinceChange:undefined,branch:develop',methods=['GET'])
def get_uitlities_pending_response():
    return jsonify(changes14)


@app.route('/app/teamcity/builds/buildType:(id:Maintenance),running:any,branch:develop', methods=['GET'])
def get_maintenance():
    number = random.randint(1, 3)
    print number
    if number == 1:
        return jsonify(maintenance_running_response)
    if number == 2:
        return jsonify(maintenance_pending_response)
    if number == 3:
        return jsonify(maintenance_finished_response)

@app.route('/app/teamcity/builds/buildType:(id:Maintenance),running:any,branch:develop,status:SUCCESS', methods=['GET'])
def get_maintenance_last_successful():
    number = random.randint(1, 3)
    print number
    if number == 1 :
        return jsonify(maintenance_running_response)
    if number == 2:
        return jsonify(maintenance_pending_response)

@app.route('/app/teamcity/builds/buildType:(id:Maintenance),sinceChange:undefined,branch:develop',methods=['GET'])
def get_maintenance_pending_response():
    return jsonify(changes14)

@app.route('/app/teamcity/builds/buildType:(id:Coverage),running:any,branch:develop', methods=['GET'])
def get_codecoverage():
  return jsonify(coverage_response)


@app.route('/app/teamcity/builds/buildType:(id:Bugs),running:any,branch:develop', methods=['GET'])
def get_bugscoverage():
  return jsonify(bugs_response)


@app.route('/app/teamcity/builds/buildType:(id:Vulnerabilities),running:any,branch:develop', methods=['GET'])
def get_vulnerabilitycoverage():
  return jsonify(vulnerabilities_response)


@app.route('/app/teamcity/builds/buildType:(id:CodeSmells),running:any,branch:develop', methods=['GET'])
def get_codesmellscoverage():
  print datetimeNow
  return jsonify(codeSmells_response)

@app.route('/app/teamcity/builds/buildType:(id:UDS),running:any,branch:uat_1.2', methods=['GET'])
def get_uds():
  number = random.randint(1, 3)
  print number
  if(number == 1) :
    return jsonify(uds_response)
  if(number == 2) :
    return jsonify(uds_response_starting)
  if (number == 3):
    return jsonify(uds_response_down)

@app.route('/app/teamcity/builds/buildType:(id:Memory),running:any,branch:develop', methods=['GET'])
def get_memory():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return jsonify(memory1_response)
  if number == 2:
    return jsonify(memory2_response)
  if number == 3:
    return jsonify(memory3_response)


@app.route('/app/teamcity/builds/buildType:(id:Cpu),running:any,branch:develop', methods=['GET'])
def get_cpu():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return jsonify(cpu1_response)
  if number == 2:
    return jsonify(cpu2_response)
  if number == 3:
    return jsonify(cpu3_response)

@app.route('/app/teamcity/builds/buildType:(id:Diskspace),running:any,branch:develop', methods=['GET'])
def get_diskspace():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return jsonify(diskspace1_response)
  if number == 2:
    return jsonify(diskspace2_response)
  if number == 3:
    return jsonify(diskspace3_response)

@app.route('/app/teamcity/builds/buildType:(id:Database),running:any,branch:develop', methods=['GET'])
def get_database():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return jsonify(database1_response)
  if number == 2:
    return jsonify(database2_response)
  if number == 3:
    return jsonify(database3_response)

@app.route('/app/teamcity/builds/buildType:(id:DataLoad),running:any,branch:develop', methods=['GET'])
def get_dataload():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return jsonify(dataLoad1_response)
  if number == 2:
    return jsonify(dataLoad2_response)
  if number == 3:
    return jsonify(dataLoad3_response)

@app.route('/app/teamcity/builds/buildType:(id:Consumption),running:any,branch:develop', methods=['GET'])
def get_consumption():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return jsonify(consumption1_response)
  if number == 2:
    return jsonify(consumption2_response)
  if number == 3:
    return jsonify(consumption3_response)

@app.route('/app/teamcity/builds/buildType:(id:uds),branch:develop', methods=['GET'])
def get_developstatus():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return red
  if number == 2:
    return yellow
  if number == 3:
    return green

@app.route('/app/teamcity/builds/buildType:(id:cpumotor),branch:develop', methods=['GET'])
def get_cpumotor():
  number = random.randint(1, 4)
  print number
  if number == 1:
    return fiftyfive
  if number == 2:
    return thirty
  if number == 3:
    return seventy
  if number == 4:
    return ninety

@app.route('/app/teamcity/builds/buildType:(id:memorymotor),branch:develop', methods=['GET'])
def get_memorymotor():
  number = random.randint(1, 4)
  print number
  if number == 1:
    return fiftyfive
  if number == 2:
    return thirty
  if number == 3:
    return seventy
  if number == 4:
    return ninety


if __name__ == '__main__':
    app.run(debug='true')